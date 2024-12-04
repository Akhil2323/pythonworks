def multiplication_table(num,end=10):#using 10 as default value .its used when end value not return or set its take end value as 10

    for i in range(1,end+1):

        #  mult=num*i

         print(f"{num}*{i}={num*i}")

multiplication_table(3,50)