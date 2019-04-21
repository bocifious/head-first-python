#create a list containing vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#assign user's input to a variable
word = input("Provide a word to search for vowels: ")

#create empty dict for the vowels
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

#for loop to add instances of vowels to dict
for letter in word:
    if letter in vowels:
        found[letter] += 1

#printing the sorted dict of vowels
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')