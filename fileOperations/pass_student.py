f1=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\all_student.txt")

f2=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\failed_student.txt")

all_student_set=set()

fail_student_set=set()



for line in f1:
 
 line=line.rstrip("\n")
 
 all_student_set.add(line)

for line in f2:
 
 line=line.rstrip("\n")
 

 fail_student_set.add(line)


passed_student=all_student_set.difference(fail_student_set)

print(passed_student)