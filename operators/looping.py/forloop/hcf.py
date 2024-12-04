num1=int(input("enter the first number:"))

num2=int(input("enter the second number:"))

gcd=1

min_num=min(num1,num2)

for i in range(1,num1+1):

    if num1%i==0 and num2%i==0:
      
      num=i

print(f"greatest common multiple={num}")




