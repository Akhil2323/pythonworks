# read the text and split each word and print

f=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\question.txt","r")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")
    
    for w in all_words:

        words.append(w)

print(words)
 
words_count={w:words.count(w) for w in words}

nested_word_count=([v,k] for k,v in words_count.items())

print(sorted(nested_word_count,reverse=True))