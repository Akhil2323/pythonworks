# print the non century year from 1800 to 2024 using for loop
for year in range(1800,2025,1):
    if year%100!=0 and year%4==0:
        print(year)
        