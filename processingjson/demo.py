from json import load

f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\json\\employee.json")

data=load(f)

for emp in data:

    print(emp)

