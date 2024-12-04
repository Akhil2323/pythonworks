# print the duplicate words from string

text="this is a test to remove duplicate words this test is simple"

spl=text.split(" ")

print(set(spl))

text1="this simple test remove duplicate words"

text_s=set(text.split(" "))

text1_s=set(text1.split(" "))

print(text1_s.issubset(text_s))
  