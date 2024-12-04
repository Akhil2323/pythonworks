# read the txt and list the txt and print

f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)