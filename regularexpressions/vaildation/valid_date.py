from re import fullmatch

user_input=input("enter the date:")

pattern="(0?[1-9]|[12][0-9]|3[01])"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid date")

else:

    print('valid')