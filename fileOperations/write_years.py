f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\years.txt","w")

for year in range(1800,2025):

    f.write(str(year)+"\n")

f.close()