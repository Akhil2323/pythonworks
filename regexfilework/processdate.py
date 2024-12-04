from re import findall

f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\regexfilework\\date.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,content)

for date in dates:

  print(date)