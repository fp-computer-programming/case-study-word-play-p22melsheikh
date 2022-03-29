# MEE 03/28/22

# open the file 
word = open("word.txt")
file = open("file.txt","a")

word = word.readlines()
for x in word:
# Interate through the word list 

    if len(x.strip()) > 20: # remove the escape characters and checks if the word is > 20
        file.write(x)

# closes files
word.close()
file.close()