# create a function smart_sub with three parameter num1,num2,reverse 
# reverse teke boolean value
# if reverse==True then return num2-num1 else num1-num2

def smart_sub(num1,num2,reverse):

    return num2-num1 if reverse==True else num1-num2

print(smart_sub(20,30,True))

