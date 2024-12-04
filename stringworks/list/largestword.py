# print the largest word from the list
text=["apple","iphone","orange","potatto"]

long=max ([len (w) for w in text])


longest_word=[w for  w in text if len (w)==long]

print(longest_word)