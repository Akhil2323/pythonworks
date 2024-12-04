# dictionary method

# employee id,name,department,age,salary

employee={"id":10,"name":"john","department":"mechanical enigneer","age":20,"salary":35000}

print(employee.get("salary"))

print(employee.get("salry"))#using get method key value deosn't exist none is print 

employee.pop("salary")#remove key salary from the employee

print(employee)

# return all keys => key ()

for k in employee.keys():

    print(k)

# fetch values =>values()

for v in employee.values():

    print(v)

# return all keys and values =>items()

for k,v in employee.items():

    print(k,v) 