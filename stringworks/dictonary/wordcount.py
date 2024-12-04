words=["hai","hello","hai","hello"]

words_count={}

for w in words:

    if w in words_count:

        words_count[w]+=1
    
    else:

        words_count[w]=1

print(words_count)