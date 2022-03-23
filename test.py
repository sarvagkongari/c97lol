introstring=input("introduce yourself: ")
characterCount=0
wordCount=1

for s in introstring:
    characterCount+=1
    if(s==" "):
        wordCount+=1
print("number of words in the string")
print(wordCount)
print("number of characters in the string")
print(characterCount)

