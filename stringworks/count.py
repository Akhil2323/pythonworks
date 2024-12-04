#print count of string separated count how many vowels and consonants

text="pneumonoultramicroscopicsilicovolcanoconiosis"

v_count=0

c_count=0

vowel_sequence=("a","e","i","o","u")

for vo in text:

    if vo in vowel_sequence:

        v_count=v_count+1

    else:

        c_count=c_count+1

print(f"vowel count={v_count}")

print(f"consonant count={c_count}")

