# write a python program to count the occurances of each element in a list 

arr=[1,2,2,3,3,3,4]

occurances={i:arr.count(i) for i in arr}

print("occurences of each element:",occurances)