# first recursive charcter or repeated charcter in countchar.py

text="abbacb"

charcter_count={}

for ch in text:

    if ch in charcter_count:

        charcter_count[ch]+=1

        break

    else:

        charcter_count[ch]=1

print(charcter_count)