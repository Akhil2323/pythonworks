# print arr square like {10:100,20:400.....}

arr=[10,20,30,40,50]

result={} #create empty dictionary

for num in arr: #arr value store num

    square=num**2 #square the num

    result[num]=square #square and num store in empty result

print(result) 

# dictionary comprehension

# result={key:value iteration condition}

result={num:num**3 for num in arr}

print(result)

