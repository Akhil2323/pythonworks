# check first five is fibnocci
previous=0

current=1

print(previous)

print(current)

for i in range(1,4):

    next=previous+current

    previous=current

    current=next

    print(next)
