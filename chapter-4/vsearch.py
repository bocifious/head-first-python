#Function to search for vowels within a supplied word
def search_for_vowels(word):
    #this is the vowel search code from chapter 3
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    #i'm not sure why they include this for loop instead of printing found
    for vowel in found:
        print(vowel)