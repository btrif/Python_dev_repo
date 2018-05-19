s = input("Please enter a sentence:\n")
lst = s.split()

# Initialize the accumulators
count = 0
wordlengths = 0

# A for loop to go through our list

for word in lst:
    count = count + 1
    wordlengths = wordlengths + len(word)
    
avgWordLength = wordlengths / count

print("the sentence you enter had:", count, "words in it and the average word length was:", round(avgWordLength, 2), ".")
