studentmarks={
    "Rahul":{49,58, 35,64},
    "Sandeep":{80,92,94,83},
    "Sita":{44,65,76,54}}
studentname=[]
for name,marks in studentmarks.items():
    allabove60 = True
    for mark in marks:
        if mark <= 60:
            allabove60 = False
            break
    if allabove60:
        studentname.append(name)

for student in studentname:
    print(student)
