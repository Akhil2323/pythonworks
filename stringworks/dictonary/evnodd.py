# print square as value if num is even else odd cube as value 

arr=[10,20,30,40,2,3,7,8,9]

even_num={num:num**2 for num in arr if num%2==0}

odd_num={num:num**3 for num in arr if num%2!=0}

print(even_num)

print(odd_num)