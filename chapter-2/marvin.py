#assign string to variable
paranoid_android = "Marvin"

#turn the string into a list called letters
letters = list(paranoid_android)

#for loop to print each character in the list preceded by tab
for char in letters:
    print('\t', char)