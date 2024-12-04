read_year=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\years.txt","r")

f_century=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\century_year.txt","w")

f_leap=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\leap_year.txt","w")


for year in read_year:

    year=int(year)
    
    if year%100==0:

        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        f_leap.write(str(year)+"\n")

read_year.close()

f_century.close()

f_leap.close()
