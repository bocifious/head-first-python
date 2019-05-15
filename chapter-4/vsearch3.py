#Function to search for vowels and letters within a supplied phrase
#the ':str) -> set' is the annotation for the function
def search_for_vowels(phrase:str) -> set:
    #this is the vowel search code from chapter 3
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

#this function sets a default value for letters of all vowels
def search_for_letters(phrase:str, letters:str='aeiou') -> set:
    #return a set of the 'letters' found in 'phrase'
    return set(letters).intersection(set(phrase))