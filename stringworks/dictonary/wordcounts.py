# print letters count of string

text="ababcdaedh"

word_count={ch:text.count(ch) for ch in text}

print(word_count)

# print only word count 1

non_recursiv_char={k for k,v in word_count.items() if v==1}

print(non_recursiv_char)