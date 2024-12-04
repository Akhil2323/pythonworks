# reduce the ilteration count

arr=[2,3,4,5]

sum=8

left=0

right=len(arr)-1

while(left<right):

 cur_sum=arr[left]+arr[right]

 if cur_sum==sum:

    print(arr[left],arr[right])

    break

 elif cur_sum>sum:

    right-=1

 elif cur_sum<sum:

    left+=1
