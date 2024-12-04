text="world world hi hello "


words=text.split(" ")

most_frequent_word={w:words.count(w) for w in words}

print(max(most_frequent_word))