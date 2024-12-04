# print the elements to add to get sum=8
arr=[2,3,4,5]

sum=8

for i in range(0,len(arr)-1):

  for j in range(i+1,len(arr)):

     cur_sum=arr[i]+arr[j]

     if sum==cur_sum:

       print(arr[i],arr[j])

       break
      
     

    
