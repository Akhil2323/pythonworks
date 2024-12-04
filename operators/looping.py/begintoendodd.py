# read starting anding ending number from user and print odd numbers using while loop
begin=int(input("enter the the starting number:"))

end=int(input("enter the ending number:"))

i=begin

while(i<=end): 
    if(i%2!=0):
        print(i)

    i=i+1
