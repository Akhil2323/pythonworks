read_word=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\text.txt","r")

palindrome=open("C:\\Users\\anush\\OneDrive\\Desktop\\pythonworks\\datasets\\palindrome.txt","w")

for line in read_word:

  word=line.rstrip("\n")

  reversed_word=word[::-1]

  if word==reversed_word:
  
   palindrome.write(word+"\n")

read_word.close()

palindrome.close()