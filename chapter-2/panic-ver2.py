#set phrase and create list
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#use bracket notation to remove 'on tap' from list
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

#print new phrase
print(plist)
print(new_phrase)