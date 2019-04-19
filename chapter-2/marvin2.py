#assign string to variable
paranoid_android = "marvin, the Paranoid Android"

#turn string into a list
letters = list(paranoid_android)

#for statement to print first six characters
for char in letters[:6]:
    print('\t', char)
print()

#for statement to print last seven characters with double tab
for char in letters[-7:]:
    print('\t'*2, char)
print()

#for statement to print slice with three tabs
for char in letters[12:20]:
    print('\t'*3, char)