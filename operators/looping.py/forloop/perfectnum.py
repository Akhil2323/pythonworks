# read the number and check its perfect number

num=int(input("enter the number:"))

total=0

for i in range(1,num):

    if num%i==0:

        total=total+i


print("perfect number" if total==num else"not perfect number")