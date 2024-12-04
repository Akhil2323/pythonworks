from re import finditer

text="I have 3 cars,2 bike and 1-Cycle"

# pattern="\w" #[a-zA-Z0-9] alphanumeric

# pattern="\d" #[0-9]

# pattern="\D" #exculde [0-9] digit

# pattern="\W" #exculde [a-zA-Z0-9] alphanumeric

# 


pattern="\S" #exclude space

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())