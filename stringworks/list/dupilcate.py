arr=[1,2,4,2,4,3,4,3,5]


arr.sort()

duplicate_number=[]

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result==0:

       if arr[i] not in duplicate_number:
           
           duplicate_number.append(arr[i])
        
print(duplicate_number)

        