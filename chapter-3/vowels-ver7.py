#create a set of vowels
vowels = set('aeiou')

#provide an input for the word(s) to search for vowels
word = input("Provide a word to search for vowels: ")

#assign result of intersection between word and vowels to variable
match = vowels.intersection(set(word))

#print result of intersection
print(match)