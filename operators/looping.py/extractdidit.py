# read the number from user and extract each digit in back to end
num=int(input("enter the number:"))

while(num!=0):
    digit=num%10
    print(digit)
    num=num//10
