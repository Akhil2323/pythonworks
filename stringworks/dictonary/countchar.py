# print the charcter count of words

text="abbacb"

charcter_count={}

for ch in text:

    if ch in charcter_count:

        charcter_count[ch]+=1

    else:

        charcter_count[ch]=1

print(charcter_count)