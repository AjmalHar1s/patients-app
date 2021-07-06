from flask import *
import pymysql
app = Flask (__name__)
app.secret_key="abc"
con=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='docondoor')
cmd=con.cursor()



@app.route ('/')
def main():
    return render_template('index.html')



#login page code
@app.route('/logincode', methods=['post'])
def logincode():
    username=request.form['textfield']
    print(username)
    password=request.form['textfield2']
    print(password)
    cmd.execute("SELECT * FROM login WHERE username='"+username+"' and PASSWORD='"+password+"'")
    res=cmd.fetchone()
    session['lid']=res[0]
    if res is None:
        return '''<script>alert('invalid user');window.location='/'</script>'''
    else:
        if(res[3]=='admin'):
            return '''<script>alert('login success');window.location='/admin_home'</script>'''
        elif(res[3]=='hospital'):
            return '''<script>alert('login success');window.location='/hospital_home'</script>'''
        elif(res[3]=='pharmacy'):
            session['lid']=res[0]
            return '''<script>alert('login success');window.location='/pharmacy_home'</script>'''
        else:
            return '''<script>alert('invalid user');window.location='/'</script>'''


#Admin Properties
@app.route ('/admin_home')
def admin_home():
    return render_template('Admin/admin_home.html')


#register and manage hospitals
@app.route ('/hospital_details')
def hospital_details():
    cmd.execute("select * from hospital")
    s = cmd.fetchall()
    return render_template('Admin/register_and_manage_hospital/hospital_details.html', res = s)

@app.route ('/hospital_registration', methods=['post'])
def hospital_registration():
    return render_template('Admin/register_and_manage_hospital/hospital_registration.html')

#hospital registration to view details code
@app.route ('/hospital_reg_code', methods=['post'])
def hospital_reg_code():
    hospital=request.form['textfield']
    place=request.form['textfield2']
    phonenumber=request.form['textfield3']
    emailid=request.form['textfield4']
    zipcode=request.form['textfield5']
    username=request.form['textfield6']
    password=request.form['textfield7']
    cmd.execute("INSERT INTO login(username, password, user_type) VALUES('"+username+"', '"+password+"', 'hospital')")
    lid=con.insert_id()
    cmd.execute("INSERT INTO hospital(login_id, hospital_name, place, email, phone_number, zip_code) VALUES('"+str(lid)+"', '"+hospital+"', '"+place+"', '"+emailid+"', '"+phonenumber+"', '"+zipcode+"')")
    con.commit()
    return '''<script>alert('registration success');window.location='/hospital_details'</script>'''

#pharmacy management
@app.route ('/pharmacy_details',methods=['get','post'])
def pharmacy_details():

    return render_template('Admin/pharmacy_management/pharmacy_details.html')

#checking whether pharmacy is private or hospital
@app.route ('/pharmacyview_details',methods=['get','post'])
def pharmacyview_details():
    type=request.form['select']
    if type=="Private":
              cmd.execute("select * from pharmacy where `hospital_id` is NULL")
              s = cmd.fetchall()
    else:
        cmd.execute("select * from pharmacy where `hospital_id` IS NOT NULL")
        s = cmd.fetchall()
    return render_template('Admin/pharmacy_management/pharmacy_details.html', res = s)

@app.route ('/pharmacy_registration', methods=['post'])
def pharmacy_registration():
    cmd.execute("SELECT * FROM `hospital`")
    s=cmd.fetchall()
    return render_template('Admin/pharmacy_management/pharmacy_registration.html',val=s)






# Edited values submitting(hospital details)
@app.route("/submit_edit_doctor", methods =['get', 'post'])
def submit_edit_doctor():
    did = session['doc_id']
    doctor_name = request.form['textfield']
    #hospital_place = request.form['textfield2']
    doctor_qualification = request.form['textfield2']
    doctor_phonenumber = request.form['textfield3']
    doctor_emailid = request.form['textfield4']
    doctor_zipcode = request.form['textfield5']
    cmd.execute("Update doctor set doctor_name = '"+doctor_name+"' , email =  '"+doctor_emailid+"' , phone_number = '"+doctor_phonenumber+"', zip_code = '"+doctor_zipcode+"' where hospital_id = '"+str(did)+"' ")
    con.commit()
    return redirect('doctor_details')

#for deleting docotor details along with login details
@app.route("/delete_doctor_details", methods=['get', 'pos'])
def delete_doctor_details():
    did = request.args.get('id')
    cmd.execute("delete from doctor where login_id = '"+str(did)+"'")
    cmd.execute("DELETE FROM `login` WHERE `logid_id`='"+str(did)+"'")
    con.commit()
    return redirect('doctor_details')

#checking whether doctor is private or hospital
@app.route ('/doctoriew_details',methods=['get','post'])
def doctorview_details():
    type=request.form['select']
    if type=="Private":
        # cmd.execute("SELECT `doctor`.*,`department`.`doctor_department` FROM `department` JOIN `doctor` ON `doctor`.`department_id`=`department`.`department_id` is NULL")

        # cmd.execute("select * from doctor where `hospital_id` is NULL")
        cmd.execute("SELECT doctor.*, department.doctor_department FROM doctor JOIN department ON doctor.department_id = department.department_id WHERE hospital_id is NULL")
        s = cmd.fetchall()
        return render_template('Admin/doctor_management/doctor_details.html', res = s)
    elif type=="Hospital":
        cmd.execute("SELECT doctor.*, department.doctor_department FROM doctor JOIN department ON doctor.department_id = department.department_id WHERE hospital_id is NOT NULL")
        s = cmd.fetchall()
        print(s)
        return render_template('Admin/doctor_management/doctor_details.html', res = s)


@app.route ('/doctor_time_schedule')
def doctor_time_schedule():
    return render_template('Admin/doctor_management/doctor_time_schedule.html')

#feedback
@app.route ('/feedback')
def feedback():
    cmd.execute("select patient.first_name, patient.last_name, feedback.* from patient join feedback on feedback.patient_id=patient.login_id ")
    s = cmd.fetchall()
    print(s)
    return render_template('Admin/admin_view_feedback.html', val=s)



#Complaints
@app.route ('/complaints')
def complaints():
    cmd.execute("SELECT patient.first_name, patient.last_name, complaint.* FROM patient JOIN complaint ON complaint.patient_id=patient.login_id and complaint.reply='NA' ")
    s=cmd.fetchall()
    return render_template('Admin/view_complaints.html',val=s)

#Complaint_reply
@app.route('/complaint_reply', methods=['get'])
def complaint_reply():
    id=request.args.get('id')
    session['comp_id'] = id
    return render_template('Admin/complaint_reply.html')

# for sending the reply
@app.route('/send_complaint_reply', methods=['post'])
def send_complaint_reply():
    reply=request.form['textarea']
    cmd.execute("update complaint set reply='"+reply+"' where complaint_id='"+str(session['comp_id'])+"'")
    con.commit()
    return'''<script>alert("Reply Send!");window.location="complaints"</script>'''



#approve private docs

@app.route ('/approve_doc')
def approve_doc():
    cmd.execute("SELECT doctor.* FROM doctor JOIN login ON doctor.login_id = login.logid_id WHERE login.user_type ='pending'")
    s = cmd.fetchall()
    return render_template("approve_doc.html",res=s)

@app.route ('/approve_d')
def approve_d():
    id = request.args.get('id')
    cmd.execute("update login SET user_type = 'doctor' WHERE logid_id = '"+str(id)+"''")
    con.commit()
    return '''<script>alert('approved');window.location='/approve_doc'</script>'''

@app.route ('/reject_d')
def reject_d():
    id = request.args.get('id')
    cmd.execute("delete from login WHERE logid_id = '"+str(id)+"''")
    cmd.execute("delete from doctor WHERE logid_id = '" + str(id) + "''")
    con.commit()
    return '''<script>alert('rejected');window.location='/approve_doc'</script>'''

















#Hospital Properties
@app.route ('/hospital_home')
def hospital_home():
    return render_template('Hospital/hospital_home.html')

#Doctors time schedule in hospitals
@app.route ('/hospital_doctor_time_schedule')
def hospital_doc_time_schedule():
    cmd.execute("select * from department")
    s = cmd.fetchall()
    return render_template('Hospital/hospital_doctor_time_schedule.html',val = s, depid=0)

#View doctor details according to department (sorting)

@app.route('/doctor_department_sort',methods=['post'])
def doctor_department_sort():
    cmd.execute("select * from department")
    f = cmd.fetchall()
    dptid = request.form['select']
    print(dptid)
    cmd.execute("select doctor_department from department where department_id='"+str(dptid)+"'")
    d=cmd.fetchone()
    cmd.execute("SELECT doctor.doctor_name,department_id,time_schedule.* FROM doctor JOIN time_schedule ON doctor.login_id = time_schedule.doctor_lid AND doctor.department_id='"+dptid+"'")
    s=cmd.fetchall()
    print(s)
    return render_template('Hospital/hospital_doctor_time_schedule.html',val1 = s,val = f,depid=d)



#inserting values into doctor table
@app.route ('/doctor_reg_code', methods=['post'])
def doctor_reg_code():
    doctor_name = request.form['textfield2']
    email_id = request.form['textfield4']
    phone_number = request.form['textfield5']
    #hospital = request.form['select2']
    zipcode = request.form['textfield7']
    gender = request.form['radiobutton']
    qualification = request.form.getlist('checkbox')
    qua=','.join(qualification)
    department = request.form['select3']
    username = request.form['textfield8']
    password = request.form['textfield3']
    cmd.execute(
        "INSERT INTO login(username, password, user_type) VALUES('" + username + "', '" + password + "', 'doctor')")
    did = con.insert_id()
    cmd.execute("INSERT INTO `doctor` VALUES(null,'"+str(did)+"','"+department+"','"+str(session['lid'])+"','"+doctor_name+"','"+email_id+"','"+qua+"','"+phone_number+"','"+gender+"','"+zipcode+"')")
    con.commit()
    return '''<script>alert('registration success');window.location='/doctor_details'</script>'''


#edit doctor registration and details

@app.route('/edit_doctor')
def edit_doctor():
    did = request.args.get('id')
    session['doc_id'] = did
    cmd.execute("select * from doctor where doctor_id = '"+str(did)+"' ")
    val = cmd.fetchone()
    return render_template("Admin/doctor_management/doctor_details_edit.html", v = val)


#doctor_management
@app.route ('/doctor_details')
def doctor_details():
    cmd.execute(
        "SELECT doctor.*, department.doctor_department FROM doctor JOIN department ON doctor.department_id = department.department_id WHERE hospital_id is NOT NULL")
    # cmd.execute("SELECT `doctor`.*,`department`.`doctor_department` FROM `department` JOIN `doctor` ON `doctor`.`department_id`=`department`.`department_id`")
    s = cmd.fetchall()
    return render_template('Admin/doctor_management/doctor_details.html', res=s)
    #return render_template('Admin/doctor_management/doctor_details.html')


@app.route ('/doctor_registration',methods=['get','post'])
def doctor_registration():
    cmd.execute("SELECT * FROM `department`")
    s=cmd.fetchall()
    return render_template('Admin/doctor_management/doctor_registration.html',val=s)










#View and add patients
@app.route ('/patient_details')
def patient_details():
    cmd.execute("SELECT * FROM `patient`")
    s = cmd.fetchall()
    return render_template('Hospital/patient_details.html', val = s)

#Registration of patient in hospitals
# @app.route ('/patient_registration')
# def patient_registration():
#     return render_template('Hospital/patient_registration.html')

#Patient registration and adding to data base

# @app.route('/patient_reg_code')
# def patient_reg_code():
#     patient_name = request.form['textfield']
#     gender = request.form['radiobutton']
#     age = request.form['textfield2']
#     phone_number = request.form['textfield3']
#     email = request.form['textfield4']
#     zip_code = request.form.getlist('textfield5')
#     username = request.form['textfield6']
#     password = request.form['textfield7']
#     cmd.execute()


#View booking details of patient
@app.route ('/patient_booking_details')
def patient_booking_details():
    cmd.execute("SELECT patient.`first_name`,`last_name`,`doctor`.`doctor_name`,`booking`.* FROM `patient` JOIN `booking` ON `booking`.`patient_id`=`patient`.`login_id` JOIN `doctor` ON `doctor`.`login_id`=`booking`.`doctor_id`")
    s = cmd.fetchall()
    return render_template('Hospital/patient_booking_details.html', val=s)


#Pharmacy Properties
@app.route ('/pharmacy_home')
def pharmacy_home():
    return render_template('Pharmacy/pharmacy_home.html')

#Pharmacy management (add and delete medicine)
@app.route ('/add_and_manage_medicine')
def add_and_manage_medicine():
    cmd.execute("select * from medicine")
    s = cmd.fetchall()
    return render_template('Pharmacy/add_and_manage_medicine.html', val = s)

#Pharmacy registration
@app.route ('/pharmacy_registration1')
def pharmacy_registration1():
    return render_template('Pharmacy/pharmacy_registration.html')

#Add button in add and manage medicine to register new medicines
@app.route('/medicine_registration', methods=["post"])
def medicine_registration():
    return render_template('Pharmacy/medicine_registration.html')

#adding medicine details into registration
@app.route('/medicine_reg_code', methods=["post"])
def medicine_reg_code():
    medicine_name = request.form['textfield']
    medicine_brand = request.form['textfield2']
    manufacture_date = request.form['textfield3']
    expiry_date = request.form['textfield4']
    quantity = request.form['textfield5']

    cmd.execute("INSERT INTO medicine(medicine_id, pharmacy_id, medicine_name, medicine_brand, manufacture_date, expiry_date, quantity) VALUES(null,'"+str(session['lid'])+"' , '" + medicine_name + "', '" + medicine_brand + "', '" + manufacture_date + "', '" + expiry_date + "', '" + quantity + "') ")
    con.commit()
    return '''<script>alert('registration success');window.location='/add_and_manage_medicine'</script>'''


#for editing the registered medicedit_medicine_detailsine details
@app.route('/edit_medicine_details', methods=['get'])
def edit_medicine_details():
    mid = request.args.get('id')
    session['medi_id'] = mid
    cmd.execute("select * from medicine where medicine_id = '" + str(mid) + "' ")
    val = cmd.fetchone()
    return render_template("Pharmacy/edit_medicine_details.html", v =val)


#Editted values submitting for medicine
@app.route("/submit_edit_medicine",methods =['get','post'])
def submit_edit_medicine():
    mid = session['medi_id']
    medicine_name = request.form['textfield']
    medicine_brand = request.form['textfield2']
    manufacture_date = request.form['textfield3']
    expiry_date = request.form['textfield4']
    quantity = request.form['textfield5']
    cmd.execute("Update medicine set medicine_name = '"+medicine_name+"' ,medicine_brand =  '"+medicine_brand+"', manufacture_date =  '"+manufacture_date+"' , expiry_date = '"+expiry_date+"', quantity = '"+quantity+"' where medicine_id = '"+mid+"' ")
    con.commit()
    return redirect('add_and_manage_medicine')


#for deleting medicine details
@app.route("/delete_medicine_details", methods=['get', 'pos'])
def delete_medicine_details():
    mid = request.args.get('id')
    cmd.execute("DELETE FROM `medicine` WHERE `medicine_id`='"+str(mid)+"'")
    con.commit()
    return redirect('add_and_manage_medicine')

#View Prescriptions details of patient
@app.route ('/medicine_prescription')
def medicine_prescription():
    cmd.execute("SELECT patient.first_name, patient.last_name, medicine.medicine_name, prescription.consumption_amount, prescription.quantity ,`medicine_booking`.`medicine_booking_id` FROM patient JOIN prescription ON prescription.patient_id = patient.login_id JOIN medicine ON medicine.medicine_id = prescription.medicine_id JOIN `medicine_booking` ON `medicine_booking`.`prescription_id`=`prescription`.`prescription_id` WHERE  `medicine_booking`.`status`='pending' AND `medicine_booking`.`pharmacy_id`='"+str(session['lid'])+"'")
    s = cmd.fetchall()
    print(s)
    return render_template('Pharmacy/medicine_prescription.html', val = s)



#inserting pharmacy details into tables
@app.route('/pharmacy_reg_code', methods=['post'])
def pharmacy_reg_code():
    pharmacyname=request.form['textfield']
    place=request.form['textfield2']
    phonenumber=request.form['textfield3']
    email=request.form['textfield4']
    zipcode=request.form['textfield5']
    username=request.form['textfield6']
    password=request.form['textfield7']
    cmd.execute("INSERT INTO login(username, password, user_type) VALUES('" + username + "', '" + password + "','pharmacy')")
    lid = con.insert_id()
    cmd.execute("INSERT INTO pharmacy(login_id, pharmacy_name, email, phone_number,place,zip_code) VALUES('" + str(lid) + "', '" + pharmacyname + "', '" + email + "', '" + phonenumber + "', '" + place+ "', '" + zipcode + "')")
    con.commit()
    return '''<script>alert('registration success');window.location='/pharmacy_details'</script>'''


# edit hospital registration and details

@app.route('/edit_hospital')
def edit_hospital():
    hid = request.args.get('id')
    session['hosp_id'] = hid
    cmd.execute("select * from hospital where hospital_id = '"+str(hid)+"' ")
    val = cmd.fetchone()
    return render_template("Admin/register_and_manage_hospital/hospital_details_edit.html", v = val)


# Edited values submitting(hospital details)

@app.route("/submit_edit_hospital", methods =['get', 'post'])
def submit_edit_hospital():
    hid = session['hosp_id']
    hospital_name = request.form['textfield']
    hospital_place = request.form['textfield2']
    hospital_phonenumber = request.form['textfield3']
    hospital_emailid = request.form['textfield4']
    hospital_zipcode = request.form['textfield5']
    cmd.execute("Update hospital set hospital_name = '"+hospital_name+"' ,place =  '"+hospital_place+"', email =  '"+hospital_emailid+"' , phone_number = '"+hospital_phonenumber+"', zip_code = '"+hospital_zipcode+"' where hospital_id = '"+hid+"' ")
    con.commit()
    return redirect('hospital_details')

#for deleting hospital details along with login details
@app.route("/delete_hospital_details", methods=['get', 'pos'])
def delete_hospital_details():
    hid = request.args.get('id')
    cmd.execute("delete from hospital where login_id = '"+str(hid)+"'")
    cmd.execute("DELETE FROM `login` WHERE `logid_id`='"+str(hid)+"'")
    con.commit()
    return redirect('hospital_details')


# edit pharmacy registration and details
@app.route('/edit_pharmacy',methods=['get'])
def edit_pharmacy():
    pid = request.args.get('id')
    session['pharm_id'] = pid
    cmd.execute("select * from pharmacy where pharmacy_id = '"+str(pid)+"' ")
    val = cmd.fetchone()
    return render_template("Admin/pharmacy_management/pharmacy_details_edit.html", v = val)

#Editted values submitting for pharmacy
@app.route("/submit_edit_pharmacy",methods =['get','post'])
def submit_edit_pharmacy():
    pid = session['pharm_id']
    pharmacy_name = request.form['textfield']
    pharmacy_place = request.form['textfield2']
    pharmacy_phonenumber = request.form['textfield3']
    pharmacy_emailid = request.form['textfield4']
    pharmacy_zipcode = request.form['textfield5']
    cmd.execute("Update pharmacy set pharmacy_name = '"+pharmacy_name+"' ,place =  '"+pharmacy_place+"', email =  '"+pharmacy_emailid+"' , phone_number = '"+pharmacy_phonenumber+"', zip_code = '"+pharmacy_zipcode+"' where pharmacy_id = '"+pid+"' ")
    con.commit()
    return redirect('pharmacy_details')

#for deleting pharmacy details along with login details
@app.route("/delete_pharmacy_details", methods=['get', 'pos'])
def delete_pharmacy_details():
    pid = request.args.get('id')
    cmd.execute("delete from pharmacy where login_id = '"+str(pid)+"'")
    cmd.execute("DELETE FROM `login` WHERE `logid_id`='"+str(pid)+"'")
    con.commit()
    return redirect('pharmacy_details')









































if __name__== '__main__':
                app.run(debug=True)