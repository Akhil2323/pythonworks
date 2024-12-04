text="hello python"

print(text.capitalize())#print the string  first letter uppercase

text="HELLO PYTHON"

print(text.casefold())#print the string all character lowercase

text="hellopython"

print(text.isalpha())#check string only contain alphabetic 

text="12345hello"

print(text.isdigit())#check string only contain digit

text="hellopython123"

print(text.isalnum())#check string contain both alphabetic and digit

text="hellopython"

print(text.endswith("on"))#check last character end with  on

print(text.startswith("he"))#check first character start with he



for abc in text:#print each character in the string 

    print(abc)
