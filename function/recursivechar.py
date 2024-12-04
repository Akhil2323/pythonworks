# print most recurive character and least recursive character

text="ABAABBC"

def get_count(ch):

    return text.count(ch)

most_frequent_character=max(text,key=get_count)

print(most_frequent_character)

least_frequent_character=min(text,key=get_count)

print(least_frequent_character)
