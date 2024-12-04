# print the balance text after merge

text1="PQRST"

text2="ABC"

smallest_text=text1 if text1<text2 else text2

largest_text=text1 if text1>text2 else text2

balance_text=largest_text[len(smallest_text):]

print(balance_text)
