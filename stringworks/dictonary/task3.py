# print name and average marks of each student
student_data={
  "hari":[40,45,35],
  "vipin":[34,40,35],
  "vinay":[40,45,35],
  "bijoy":[33,38,35],
  "anvin":[32,30,40]
}

stud_av_mrk={k:sum(v)/len(v) for k,v in student_data.items()}

print(stud_av_mrk)