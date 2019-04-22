#create a list containing vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#assign user's input to a variable
word = input("Provide a word to search for vowels: ")

#create empty dict for the vowels
found = {}

#for loop to add instances of vowels to dict
for letter in word:
    if letter in vowels:
        #setdefault used to initalize vowels in found dict
        found.setdefault(letter, 0)
        found[letter] += 1

#printing the sorted dict of vowels
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')