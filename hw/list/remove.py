# write a python program to remove duplicates from a list

arr=[1,2,2,1,2,4,5,8,4,3,6]

arr.sort()

single_num=list(set(arr))

print("list with duplicate removed:",single_num)