# exclude the a and k print all other alphbets

from re import finditer

text="I have 3 cars,2 bike and 1 cycle"


# pattern="[^ak]" #exclude a and k

# matcher=finditer(pattern,text)

# for obj in matcher:

#     print(obj.start(),obj.group())


pattern="[^a-zA-Z0-9]" #exclude all upper and lower  case and digits

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())