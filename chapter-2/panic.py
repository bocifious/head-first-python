#set initial phrase and make it a list
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#remove last four characters easily
for i in range(4):
    plist.pop()

#set a new list with the letters we want
found = ['o', 'n', 't', 'a', 'p']

#use for loop to remove the letters not in found list
for letter in plist:
    if letter not in found:
        plist.remove(letter)

#remove and swap the last two characters
plist.extend([plist.pop(), plist.pop()])

#create new phrase to print out
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)