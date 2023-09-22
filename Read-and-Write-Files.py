#This code reads the user's text file, alter it and writes a new file with the corrections done.

try:
    with open('file.txt', 'r') as file:  # Open the file for reading.
        text = file.read()  # Read the contents of the file under the variable 'text'.

    char_up = text.upper()  # Convert the text to uppercase using the .upper() function.
    char_len = len(text)  # Count the total number of characters in text using the len() function.

    vowels = ['a', 'e', 'i', 'o', 'u']  # Place 'a', 'e', 'i', 'o', and 'u' under vowels.
    new_text = ''.join(['*' if char.lower() in vowels else char for char in char_up])  # Replace all vowels with asterisk.

    with open('new_text.txt', 'w') as file:  # Write the modified text to a new file.
        file.write(new_text)
        file.write(f"\nTotal number of characters: {char_len}")

#  Make sure to handle any possible errors that may occur during file reading, writing or string operations with appropriate exception handling.
except FileNotFoundError:
    print("Error. File not found")
else:
    pass
finally:
    pass

