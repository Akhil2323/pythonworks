# create dictionary employee with key eid,name,salary,department,experience

employee={"eid":10,"name":"abhi","salary":20000,"department":"hr","experience":6}

print(employee)

# print slary of employee

print(employee["salary"])

# add contact as 146780

employee["contact"]=146780

print(employee)

# if experience > 5 update salary as current_salary+10000 else current_salary+5000

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)
 
# add role as SDE if exp>5 else add role as JDE

if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)