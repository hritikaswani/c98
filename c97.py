name=input("what is your name?")
characterCount=0
wordCount=0
for i in name:
    characterCount+=1
    print(characterCount)
    if (i==" "):
        wordCount+=1
print("number of words in the string:")
print(wordCount+1)
print("number of characters in the string:")
print(characterCount+1)


