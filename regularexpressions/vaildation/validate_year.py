from re import fullmatch

year=input("enter year:")

pattern="((18|19)[0-9]{2}|200[0-9]{1}|202[1234])"

matcher=fullmatch(pattern,year)

if matcher==None:

    print("invalid year")

else:

    print("valid year")