#create two numbers
num1=100
num2=200
print(f"value before swapping num1={num1} , num2={num2}")

#first logic
# temp=num1
# num1=num2
# num2=temp

#second logic(it only used for numbers)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"value after swapping num1={num1} num2={num2}")