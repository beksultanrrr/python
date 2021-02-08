word = input()
vowels = 0
consonants = 0
for i in word:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
    else:
        consonants += 1
print(word.replace(vowels,'.'))
