# print each array in single list. arr has 2 list ,list inside another list
arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50],
    ]

arr_list=[num for ls in arr for num in ls ]

print(arr_list)