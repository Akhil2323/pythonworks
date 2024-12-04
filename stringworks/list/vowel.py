# print the words first letter start with vowel from the list
text=["orange","iphone","apple","potatto"]

vowel_word=[w for w in text if w[0] in ['a','e','i','o','u']]

print("vowel",vowel_word)

consonant_word=[w for w in text if w[0] ]not in ['a','e','i','o','u']

print(consonant_word)

