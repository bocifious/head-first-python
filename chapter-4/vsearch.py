#Function to search for vowels within a supplied word
#the ':str) -> set' is the annotation for the function
def search_for_vowels(phrase:str) -> set:
    #this is the vowel search code from chapter 3
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
