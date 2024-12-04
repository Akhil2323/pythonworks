# print array like this arr=[100,800,300,600,500,400,700,200]
arr=[100,200,300,400,500,600,700,800]

#method 1

odd_position=[arr[i] for i in range(0,len(arr)) if i%2!=0]


for i in range(1,len(arr),2):

    element=odd_position.pop()

    arr[i]=element

print(arr)

# method 2``````````````
left=1

right=len(arr)-1

if right%2==0:

    right-=1

while(left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left+=2

    right-=2

print(arr)