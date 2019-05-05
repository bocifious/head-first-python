#create a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#provide input that is assigned to variable
word = input("Provide a word to search for vowels: ")

#create empty list for matches
found = []

#for loop to find vowels in word and append them to empty found list
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

#print vowels that are also in found list
for vowel in found:
    print(vowel)
