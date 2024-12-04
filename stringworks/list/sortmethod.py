# lst=[2,6,4,8,3,5,9,1]

# lst.sort()

# print(lst)

# # print in decending order

# lst.sort(reverse=True)

# print(lst)

arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

for i in range(0,len(arr1)):

    for j in range(0,len(arr2)):

       if arr1[i]==arr2[j]:
         
         print(arr1[i])
           
         break