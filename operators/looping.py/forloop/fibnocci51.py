 # check 51 is fibnocci
number=int(input("enter the number:"))

check=number

previous=0

current=1

is_fibo=False

for i in range(1,number+1):

    next=previous+current

    previous=current

    current=next

    if check==next:

        is_fibo=True

        break
print(is_fibo)
