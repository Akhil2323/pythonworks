# check the string contain all alphabetic lettrs

text="The quick brown fox jumps over the lazy dog".casefold()

alpabets="abcdefghijklmnopqrstuvwxyz"

is_pangram=True

for ch in alpabets:

    if ch not in text:

        is_pangram=False

        break

print(is_pangram)

