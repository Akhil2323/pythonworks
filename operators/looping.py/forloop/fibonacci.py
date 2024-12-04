# print fibonacci series 7

previous=0

current=1

print(previous)

print(current)

for i in range(1,6):

    next=previous+current

    previous=current

    current=next

    print(next)
