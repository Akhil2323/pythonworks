# write a python program to find the common elements in two lists

arr1=[1,2,3,4,5,6,7]

arr2=[2,4,6,8,9,10]

a1=0

a2=0

while(a1<len(arr1) and a2<len(arr2)):

    if arr1[a1]==arr2[a2]:

        print(arr2[a2])

        a1+=1

        a2+=1

    elif arr1[a1]<arr2[a2]:

        a1+=1

    elif arr1[a1]>arr2[a2]:

        a2+=1
