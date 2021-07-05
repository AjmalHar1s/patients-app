from flask import *
import pymysql
app = Flask (__name__)
app.secret_key="abc"
from src.miningdoc import selection

con=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='docondoor')
cmd=con.cursor()




## login
@app.route('/login', methods = ['post'])
def login():
    username = request.form['name']
    password = request.form['pwd']
    cmd.execute("select * from login where username ='"+username+"' and password = '"+password+"'")
    res = cmd.fetchone()
    print(res)
    if res is None:
        return jsonify({'result':"invalid"})
    else:
        return jsonify({'result':str(res[0])+"#"+res[3]})



## DOCTOR ADD TIME

@app.route('/add_doctor_time', methods = ['post'])
def add_doctor_time():
    doclid=request.form['doc_lid']
    fromtime=request.form['from_time']
    totime=request.form['to_time']
    day=request.form['day']
    cmd.execute("insert into time_schedule values(null,'"+str(doclid)+"','"+fromtime+"','"+totime+"','"+day+"')")
    con.commit()
    return jsonify({'result': "success"})


##view dc time


@app.route('/view_doc_time',methods=['POST'])
def view_doc_time():
    lid=request.form['lid']
    cmd.execute("SELECT * FROM `time_schedule` WHERE `time_schedule`.`doctor_lid`='"+lid+"'")
    s = cmd.fetchone()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)




## Edit Time

@app.route('/edit_time', methods=['post'])
def edit_time():
    doclid = request.form['doclid']
    fromtime = request.form['fromtime']
    totime = request.form['totime']
    day = request.form['day']
    cmd.execute("update into time_schedule SET from_time = '"+fromtime+"', to_time = '"+totime+"', day='"+day+"' WHERE doclid='"+doclid+"' ")
    return jsonify({'result': "success"})






## Delete time

@app.route('/delete_time', methods = ['post'])
def delete_time():
    doclid = request.form['doclid']

    cmd.execute("delete from  time_schedule WHERE doclid='" + doclid + "' ")
    return jsonify({'result': "success"})


## view patient (doc) to chat

@app.route('/view_patient_to_chat', methods = ['post'])
def view_patient_to_chat():
    did = request.form['doc_id']
    cmd.execute("SELECT`patient`.* FROM `patient` JOIN`booking` ON patient.login_id = `booking`.`patient_id` WHERE `booking`.`doctor_id` ='"+str(did)+"' group by patient.login_id  ")
    s=cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)


## Chat with patient(doc)

@app.route('/chat', methods = ['post'])
def chat():
    fromid = request.form['from_id']
    toid = request.form['toid']
    message = request.form['msg']
    cmd.execute("Insert into chat values (null,'"+fromid+"','"+toid+"', '"+message+"', CURDATE())")
    con.commit()

    return 'success'




## view chat

@app.route('/view_chat', methods = ['post'])
def view_chat():
    uid = request.form['uid']
    fid = request.form['fid']
    cmd.execute("select * from chat where (from_id='" + str(uid) + "' and to_id='" + str(fid) + "') or (from_id='" + str(
        fid) + "' and to_id='" + str(uid) + "') order by date asc")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)

## view doctor (patient) to chat

@app.route('/view_doctor_to_chat', methods = ['post'])
def view_doctor_to_chat():
    docid = request.form['docid']
    cmd.execute("select * from  doctor WHERE doctor_id='" + docid + "' ")
    return jsonify({'result': "success"})




## view patient
@app.route('/viewprofile', methods = ['post'])
def viewprofile():
    con = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='docondoor')
    cmd = con.cursor()
    lid = request.form['lid']
    print(lid)
    cmd.execute("select * from  patient WHERE login_id='" + lid + "' ")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)


## view doctor
@app.route('/viewprofile_doc', methods = ['post'])
def viewprpfile_doc():
    dlid = request.form['dlid']
    print(dlid)
    cmd.execute("select * from  doctor WHERE login_id='" + dlid + "'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)





### Update profile
@app.route('/update_profile', methods = ['post'])
def update_profile():
    fname = request.form['fname']
    lname = request.form['lname']
    dob = request.form['dob']
    gender = request.form['gender']
    email = request.form['email']
    phone = request.form['phone']
    place = request.form['place']
    lid = request.form['lid']
    cmd.execute(" update patient SET first_name  = '"+fname+"' , last_name = '"+lname+"', date_of_birth = '"+dob+"', gender ='"+gender+"',email = '"+email+"',phone_number = '"+phone+"',place ='"+place+"' where login_id = '"+lid+"'")
    con.commit()
    return jsonify({'result': "success"})



### Update profile doctor
@app.route('/update_profile_doc', methods = ['post'])
def update_profile_doc():
    doc_name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    qualification = request.form['qualification']
    dep_id = request.form['did']
    phone = request.form['phone']
    lid = request.form['lid']
    print("update doctor SET doctor_name  = '"+doc_name+"' , email = '"+email+"', qualification ='"+qualification+"',phone_number = '"+phone+"',gender ='"+gender+"',department_id ='"+dep_id+"'  where login_id = '"+lid+"'")
    cmd.execute(" update doctor SET doctor_name  = '"+doc_name+"' , email = '"+email+"', doctor_qualification ='"+qualification+"',phone_number = '"+phone+"',gender ='"+gender+"',department_id ='"+dep_id+"'  where login_id = '"+lid+"'")
    con.commit()
    return jsonify({'re': "success"})




## Doctor booking

@app.route('/doctor_booking', methods = ['post'])
def doctor_booking():
    pid = request.form['login_id']
    docid = request.form['doctor_id']

    cmd.execute("Insert into booking values(null,'" + pid + "','" + docid + "',curdate(),curtime(),'200','pending') ")
    con.commit()
    return jsonify({'result': "success"})


## doctor view booking
@app.route('/doctor_view_booking', methods = ['post'])
def doctor_view_booking():
    docid = request.form['docid']
    cmd.execute("SELECT booking.*,`patient`.`first_name`,`patient`.`last_name`,`patient`.`phone_number` FROM `patient` JOIN `booking` ON `booking`.`patient_id`=`patient`.`login_id` WHERE `booking`.`doctor_id`='"+docid+"'")
    s = cmd.fetchone()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)

## Accept Patient
@app.route('/accept_patient', methods = ['post'])
def accept_patient():
    bid = request.form['bid']
    cmd.execute("update booking SET b_status  = 'accepted' WHERE booking_id = '"+str(bid)+"'")
    con.commit()
    return jsonify({'result': "success"})





## Reject patient

@app.route('/reject_patient', methods = ['post'])
def reject_patient():
    bid = request.form['bid']
    cmd.execute("update booking SET b_status  = 'rejected' WHERE booking_id = '" + str(bid) + "'")
    con.commit()
    return jsonify({'result': "success"})






## view payment (doc)

@app.route('/view_payment_doc', methods = ['post'])
def view_payment_doc():
    doc_id = request.form['doc_id']
    cmd.execute("SELECT `patient`.`first_name`,`patient`.`last_name`,`payment`.* FROM `patient` JOIN `booking` ON booking.patient_id = patient.login_id JOIN payment ON payment.booking_id = booking.`booking_id` WHERE booking.doctor_id='"+doc_id+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)





## view_payment_(patient)

@app.route('/view_payment_patient', methods = ['post'])
def view_payment_patient():
    pid = request.form['pid']
    print(pid)
    cmd.execute("SELECT `doctor`.`doctor_name`,`payment`.* ,patient.*FROM `doctor` JOIN `booking` ON booking.`doctor_id` = `doctor`.login_id JOIN payment ON payment.booking_id = booking.`booking_id` join patient on patient.login_id = booking.patient_id and  booking.`patient_id`='"+str(pid)+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)


##payment do

@app.route('/payment', methods = ['post'])
def payment():
    login_id = request.form['login_id']
    account_no = request.form['Account_no']
    ifsc = request.form['Ifsc']
    bank = request.form['Bank_name']
    pin = request.form['Pin']
    amount = request.form['Amount']
    cmd.execute("SELECT MAX(`booking_id`) FROM `booking` WHERE patient_id = '"+login_id+"'")
    p= cmd.fetchone()
    cmd.execute("SELECT * FROM bank WHERE `account_no`='"+account_no+"'    AND `ifsc`= '"+ifsc+"'    AND `pin`= '"+pin+"'   AND `login_id`='"+login_id+"'   AND bank_name = '"+bank+"'   ")
    s= cmd.fetchone()
    if s is not None:
        print("hiiii")
        if int(s[6]) >= int(amount):
            cmd.execute("INSERT INTO `payment` VALUES (NULL,'"+str(p[0])+"' ,'paid', '"+amount+"')")
            total = int(s[6])- int(amount)
            cmd.execute("UPDATE bank SET `amount`= '"+str(total)+"'  WHERE `account_no`='"+account_no+"'     AND  `login_id` = '"+str(login_id)+"'")
            con.commit()
            return jsonify({'result': 'succcess'})
        else:
            return jsonify({'result':'insufficient balanace'})
    else:
        return  jsonify({'result' : 'fail'})









## Add prescription(doc)

@app.route('/add_prescription', methods = ['post'])
def add_prescription():

    pid = request.form['pid']
    mid = request.form['mid']
    docid = request.form['docid']
    cons_amt = request.form['cons_amt']
    date = request.form['date']
    time = request.form['time']
    cmd.execute("Insert into booking values(patient_id = '" + str(pid) + "',medicine_id = '"+str(mid)+"',doctor_id = '" + str(docid) + "',consumption_amount = '"+cons_amt+"', date = '" + date + "',time = '" + time + "')")
    con.commit()
    return jsonify({'result': "success"})
# ## View_prescription
#
#
@app.route('/view_prescription', methods = ['post'])
def view_prescription():
    lid = request.form['lid']
    pharid = request.form['pharid']
    print(lid)
    print(pharid)
    cmd.execute("SELECT `medicine`.*,`prescription` .* FROM `medicine` JOIN `prescription` ON `medicine`.`medicine_id` = `prescription`.`medicine_id` WHERE `medicine`.`pharmacy_id` = '"+pharid+"' AND `prescription`.`patient_id` = '"+lid+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    print(json_data)
    return jsonify(json_data)

##Medicine view
@app.route('/view_med', methods=['post'])
def view_med():

    con = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='docondoor')
    cmd = con.cursor()
    cmd.execute("SELECT * FROM `medicine`")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    print(json_data)
    return jsonify(json_data)


@app.route('/view_med1', methods=['post'])
def view_med1():
    print("=============================================")
    print(request.form)
    try:
        con = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='docondoor')
        cmd = con.cursor()
        name=request.form['name']
        cmd.execute("SELECT * FROM `medicine` where medicine_name like '%"+name+"%'")
        s = cmd.fetchall()
        print(s)
        row_headers = [x[0] for x in cmd.description]
        json_data = []
        for result in s:
            json_data.append(dict(zip(row_headers, result)))
        con.commit()
        print(json_data)
        return jsonify(json_data)
    except:
        con = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='docondoor')
        cmd = con.cursor()
        cmd.execute("SELECT * FROM `medicine`")
        s = cmd.fetchall()
        print(s)
        row_headers = [x[0] for x in cmd.description]
        json_data = []
        for result in s:
            json_data.append(dict(zip(row_headers, result)))
        con.commit()
        print(json_data)
        return jsonify(json_data)
## Provide location (doc)

@app.route('/provide_location', methods = ['post'])
def provide_location():
    latitude = request.form ['latitude']
    longitude = request.form ['longitude']
    logid = request.form ['logid']
    cmd.execute("Insert into location values ('"+str(logid)+"', latitude = '"+latitude+", longitude = '"+longitude+"'')")
    con.commit()
    return jsonify({'result': "success"})




## chat with chat bot for patient

@app.route('/chat_bot', methods = ['post'])
def chat_bot():
    return



## View Doctor Department

@app.route('/View_Doc_Department', methods = ['post'])
def View_Doc_Department():
    cmd.execute("SELECT `doctor`.`doctor_name`,`department`.`doctor_department` FROM doctor JOIN department ON doctor.`department_id`=`department`.`department_id`")
    s = cmd.fetchone()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)




##Payment (insert)

# @app.route('/Payment', methods = ['post'])
# def Payment():
#     booking_id = request.form['booking_id']
#     cmd.execute("Insert into payment values ('"+str(booking_id)+"','not paid')")
#     con.commit()
#     return jsonify({'result': "success"})





## Send feedback
@app.route('/send_feedback', methods = ['post'])
def send_feedback():
    pid = request.form['pid']
    feedback = request.form['feedback']

    cmd.execute("INSERT INTO feedback VALUES (NULL,'" + str(pid) + "','"+feedback+"',CURDATE(),CURTIME())")
    con.commit()
    return jsonify({'result': "success"})



## view_feedback

@app.route('/View_feedback', methods = ['post'])
def View_feedback():
    cmd.execute("SELECT feedback.*, patient.first_name,patient.last_name FROM patient JOIN feedback ON patient.login_id = feedback.patient_id")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)









## Send Complaint

@app.route('/send_Complaint', methods = ['post'])
def send_complaint():
    pid = request.form['pid']
    print(pid)
    complaint = request.form['complaint']
    # date = request.form['date']
    # time = request.form['time']
    # reply = request.form['reply']
    cmd.execute("Insert into complaint values (null,'" + str(pid) + "','" + complaint + "',curdate(),curtime(), 'pending')")
    con.commit()
    return jsonify({'re': "success"})








##View Reply

@app.route('/view_reply', methods = ['post'])
def view_reply():
    pid = request.form['pid']
    print(pid)
    cmd.execute("SELECT `patient`.`first_name`,`last_name`,`complaint`.* FROM complaint JOIN `patient` ON `patient`.`login_id`=`complaint`.`patient_id` WHERE `complaint`.patient_id = '"+str(pid)+"'")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)







## View_nearest_pharmacy

@app.route('/view_nearest_pharmacy', methods = ['post'])
def view_nearest_pharmacy():
    latitude = request.form['lati']
    print(latitude)
    longitude = request.form['longi']
    print(longitude)
    # cmd.execute("SELECT `pharmacy`.*,(3959 * ACOS ( COS ( RADIANS('" + str(latitude) + "') ) * COS( RADIANS(`latitude`) ) * COS( RADIANS(`longitude`) - RADIANS('" + str(longitude) + "') ) + SIN ( RADIANS('" + str(latitude) + "') ) * SIN( RADIANS(`latitude`) ))) AS user_distance FROM `pharmacy` HAVING user_distance  < 6.2137")
    cmd.execute("SELECT `pharmacy`.*,(3959 * ACOS ( COS ( RADIANS('" + str(latitude) + "') ) * COS( RADIANS(`latitude`) ) * COS( RADIANS(`longitude`) - RADIANS('" + str(longitude) + "') ) + SIN ( RADIANS('" + str(latitude) + "') ) * SIN( RADIANS(`latitude`) ))) AS user_distance FROM `pharmacy` HAVING user_distance  < 6.2137")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)





## Medicine Booking (insert)
@app.route('/medicine_booking', methods = ['post'])
def medicine_booking():
    pid = request.form['pid']
    mid = request.form['mid']
    pharid = request.form['pharid']
    date = request.form['date']
    time = request.form['time']
    cmd.execute("Insert into payment values ('" + str(pid) + "','" + str(mid) + "','" + str(pharid) + "','" + date + "', '" + time + "')")
    con.commit()
    return jsonify({'result': "success"})






## View_Time_schedule

@app.route('/view_time_schedule', methods = ['post'])
def view_time_schedule():
    cmd.execute("SELECT doctor_lid,from_time,to_time,DAY FROM time_schedule")
    s = cmd.fetchone()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)


## create account

@app.route('/create_account', methods = ['post'])
def create_account():
    email = request.form['email']
    password = request.form['pwd']
    password_agn = request.form['pwd_agn']
    user_type = request.form['t']
    if (user_type =='doctor'):

        if (password == password_agn):
            cmd.execute("insert into login values(null,'" + email + "','" + password + "', '" + user_type + "')");
            id=con.insert_id()

            cmd.execute("insert into doctor values(null,'"+str(id)+"',null,null,null,null,null,null,null,null)");
            con.commit()
            return jsonify({'re': "success"})
        else:
            return jsonify({'re': "password not same as above"})
    else:
        if (password == password_agn):
            cmd.execute("insert into login values(null,'" + email + "','" + password + "', '" + user_type + "')");
            id = con.insert_id()
            cmd.execute("insert into patient values(null,'"+str(id)+"',null,null,null,null,null,null,null)");
            con.commit()
            return jsonify({'re': "success"})
        else:
            return jsonify({'re': "password not same as above"})














## doctor departent view
@app.route('/doctor_dep_view', methods = ['post'])
def doctor_dep_view ():
    con = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='docondoor')
    cmd = con.cursor()
    cmd.execute("select * from department ")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)


## Doctor Registration outside hospital

@app.route('/doctor_reg_out', methods = ['post'])
def doctor_reg_out():
    department_id = request.form['did']
    doctor_name = request.form['doctor_name']
    email = request.form['email']
    doctor_qualification = request.form['doctor_qualification']
    phone_number = request.form['phone_number']
    gender = request.form['gender']
    zip_code = request.form['zip_code']
    username = request.form['username']
    password = request.form['password']

    cmd.execute("insert into login values(null,'" + username + "','" + password + "'  'pending' ")
    s=con.commit()
    cmd.execute("INSERT INTO doctor  VALUES(null,'"+str(s)+"',  '" + department_id + "',null,'" + doctor_name + "', '" + email + "', '" + doctor_qualification + "', '" + phone_number + "', '" + gender + "', '" + zip_code + "')")
    con.commit()
    return jsonify({'result': "success"})



## symptoms check
@app.route('/s_check_d_list', methods = ['post'])
def s_check_d_list():
    print("okkkkk")
    print(request.form)
    syml = request.form['sl']
    print(syml)
    res = selection(syml).split('#')
    json_data = []
    for r in res:
        cmd.execute("SELECT `doctor`.*,`time_schedule`.* ,`department`.*FROM `doctor` JOIN `time_schedule` ON `time_schedule`.`doctor_lid`=`doctor`.`login_id` JOIN `department` ON `department`.`department_id`=`doctor`.`department_id` WHERE `department`.`doctor_department`='"+r+"'")
        row_headers = [x[0] for x in cmd.description]
        results = cmd.fetchall()
        for result in results:
            json_data.append(dict(zip(row_headers, result)))
    con.commit()
    print(json_data)
    return jsonify(json_data)



## view hospitals op booking

@app.route('/view_hospital',methods=['POST'])
def view_hospital():
    cmd.execute("SELECT * FROM hospital")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)




## view docs for hospital

@app.route('/view_docs_op',methods=['POST'])
def view_docs_op():
    hid = request.form['hid']
    cmd.execute("SELECT doctor.doctor_id,doctor.doctor_name,doctor.doctor_qualification,doctor.login_id,`department`.`doctor_department`,`time_schedule`.*  FROM `department` JOIN `doctor` ON `department`.`department_id`=`doctor`.`department_id`  JOIN `time_schedule` ON `time_schedule`.`doctor_lid`=`doctor`.`login_id`  WHERE doctor.hospital_id = '"+hid+"' group by `doctor`.`login_id`")
    s = cmd.fetchall()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    con.commit()
    return jsonify(json_data)

## prescription amount and times add doctor
@app.route('/pres_doc_add', methods = ['post'])
def pres_doc_add():
    pid = request.form['pid']
    print(pid)
    mid= request.form['mid']
    print(mid)
    lid = request.form['lid']
    print(lid)
    consumption_amount = request.form['consumption_amount']
    quantity = request.form['consumption_quantity']
    cmd.execute("insert into prescription values(null,'"+str(pid)+"','"+str(mid)+"','"+str(lid)+"','"+consumption_amount+"','"+quantity+"',curdate(),curtime())")
    con.commit()
    return jsonify({'result': "success"})










if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)