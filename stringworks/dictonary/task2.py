student_data={
  "hari":[40,45,35],
  "vipin":[34,40,35],
  "vinay":[40,45,35],
  "bijoy":[33,38,35],
  "anvin":[32,30,40]
}

index=1

for i,element in enumerate(student_data):

    if i+1==index:

        marks=student_data.get(element)

        avg=sum(marks)/len(marks)

        print(avg)

       

        
