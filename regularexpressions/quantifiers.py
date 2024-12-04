from re import finditer

text="abbbbababbabaaaab"

# pattern="a{2}" #print 2 aa together in the text

# pattern="a{1,3}" #print minimum 1 a maximum 3 a

pattern="a*" #any number of a include 

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())