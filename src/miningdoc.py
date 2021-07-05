
# from src.db_connection import insert
dlist=["General medicine","gastroenterology","Cardiology","Urology","Gastro surgery","Neurology","Pulmonology","Nephroloy","Endocrinology","Ent","Ophthalmology","Ortho"]

syslis=[" fever, cough, bodypain, weakness, diabetic, decreased foot intake",
        "Abdominal pain, gas truble, vomiting, constipation, loose stool,stomach upset",
        "chest pain, pedal edema associated with breathing difficulty, chest tightness, pain in the neck, reduced ability to exercise, swelling",
        "urinary incontinance, urinary urgency, lower abdominal pain, swelling present on the prostate, urinary infection, foul-smelling urine",
        "appendicitis, hernia, abdominal pain, rectal bleeding, severe abdominal cramping, bloating",
        "severe head ache, weakness, numbness, slurring of speech, facial deviation, epilepsy",
        "breathing difficulty, cough, laboured breathing, snoring, coughing up blood ,lingering chest pain",
        "edema, breathing difficulty, decreased urine out put, increased creatinine,urea level, frothy urine",
        "uncontrolled diabetic, hyperthyroidism, hyperthyroidism, hyponatremia, electrolyte imbalance, depression",
        "earpain, throat pain, swallowing difficulty, hearing loss, nose bleeding, ear infections, head ache",
        "vision loss, Congectivitis, watering of eyes, redness of eyes, double vision, itching of eyes",
        "fracture, knee pain, joint pain, tumours, swelling, muscle spasms",
        ]
listsymsmall=[]
slis=[]
symlist=[]
for r in syslis:
    s=r.lower().replace(' ','')

    ss=s.split(',')
    for rr in ss:
        if not rr in slis:
            slis.append(rr)

    listsymsmall.append(ss)

print("slis",slis)

# val=("","Normal", "Low", "Medium", "High")
# for r in slis:
#     val = (r, "Normal", "Low", "Medium", "High")
#     qry="insert into question_options values(null,1,%s,%s,%s,%s,%s)"
#     insert(qry,val)


for r in listsymsmall:
    row=[]
    for rr in slis:
        if rr in r:
            row.append(3)
        else:
            row.append(0)
    symlist.append(row)



print(symlist)
for i in symlist:
    print(len(i))

import numpy as np




def selection(res):

    ress=res.split('#')
    resss=[]
    for r in ress:
        resss.append(r.replace(' ',''))
    row = []
    print("ress",resss)
    for r in slis:
        print(r)

        if r in resss:
            row.append(3)
        else:
            row.append(0)

    print(row)
    result="normal"
    distance=100.0
    for i in range(0,len(dlist)):

        euclidean_distance = np.linalg.norm(np.array(row) - np.array(symlist[i]))
        print(euclidean_distance, dlist[i])
        print(row)
        print(symlist[i])
        if euclidean_distance<distance:
            distance=euclidean_distance
            result=dlist[i]
        elif euclidean_distance==distance:
            result =result+"#"+ dlist[i]
    return result
# print(selection("#swelling#muscle spasms#snoring#cough"))

# from collections import Counter
# import re
# WORD = re.compile(r'\w+')

#
# res=selection([0, 3, 0, 0, 3, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# print(res)