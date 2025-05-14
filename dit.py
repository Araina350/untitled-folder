student_data={"id1":
    {"name":"Sara",
     "class":"V",
     "subject":"ENGLISH ,MATHS ,HINDI ,SCIENCE"} ,
    "id2": 
    {"name":"Surya",
     "class":"V",
     "subject":"ENGLISH ,MATHS ,HINDI ,SCIENCE"},
     "id3":
     {"name":"Aanya",
     "class":"V",
     "subject":"ENGLISH ,MATHS ,HINDI ,SCIENCE"} , 
     "id4" :
     {"name":"Aanya",
     "class":"V",
     "subject":"ENGLISH ,MATHS ,HINDI ,SCIENCE"}                  
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)        