from re import fullmatch

pancard_numbar=input("enter the pancard number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_numbar)

if matcher==None:

    print("invalid PANCARD")

else:

    print("valid PANMCARD")