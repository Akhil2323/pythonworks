# print largest length words of given words

words=["hello","hai","morning","test","apple"]

get_length=lambda word:len(word)

print(max(words,key=get_length))


text="this is a simple programming question to find word with maximum number of characters"

wordss=text.split(" ")

get_length=lambda w:len(w)

print(max(wordss,key=get_length))

# print the text in decending order according to length 

text="this is a simple programming question to find word with maximum number with characters"

word=text.split(" ")

def get_length(w):

    return len(w)

srt_words=sorted(word,key=get_length,reverse=True)

print(srt_words)

# print most frequent charcter

words=text.split(" ")

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)