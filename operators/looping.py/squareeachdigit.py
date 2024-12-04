# read number from user and extract the each digit and print total square of digits 

num=int(input("enter the number:"))
  
total=0

while(num!=0):
    digit=num%10

    square=digit**2

    total=total+square

    num=num//10

print(total)