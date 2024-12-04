from re import findall


f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\regexfilework\\url.txt")

content=f.read()

   
pattern="^https?://[^\s]+$"

urls=findall(pattern,content)

for url in urls:

    print(url)