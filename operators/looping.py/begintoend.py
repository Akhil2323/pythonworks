# print odd numbers starting to end and read starting and ending numbers.but starting is greater and ending number smaller but it print in ascending order using while Loop 

begin=int(input("enter the starting number:"))

end=int(input("enter the ending number:"))

if(begin>end):
    begin,end=end,begin

i=begin

while(i<=end):
    if i%2!=0:
        print(i)
    i=i+1
