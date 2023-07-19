# Program to print the ASCII value of the given character

# c = 'p'
c = input("Enter a character :")
print("The ASCII value of '" + c + "' is", ord(c))

#Here we have used ord() function to convert a character to an integer (ASCII value).
# This function returns the Unicode code point of that character.