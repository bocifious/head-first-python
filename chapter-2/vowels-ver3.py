#create a list with vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#user input word we want to check against vowels
word = input("Provide a word to search for vowels: ")

#creation of an empty list for found letters
found = []

#for loop to check if letter in word is a vowel
for letter in word:
    if letter in vowels:
        #add letter to found list on first occasion
        if letter not in found:
            found.append(letter)
#now we can print vowels in found to avoid duplicates
for vowel in found:
    print(vowel)
