# print largset string of two string using lambda function

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("apple","mangos"))

# print smallest string of two string using lambda function

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("apple","mangos"))

# print the differnce of two numbers 

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,200)) 