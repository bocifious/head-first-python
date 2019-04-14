#create a list with vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#set variable word to the word we want to check against vowels
word = "Milliways"

#for loop to check if letter in word is a vowel
for letter in word:
    if letter in vowels:
        print(letter)