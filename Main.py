# Get the character from the user  
character = input("Enter a character: ")  

# Check if the character is an alphabet  
if character.isalpha() and len(character) == 1:  
    print(f"'{character}' is an alphabet.")  
else:  
    print(f"'{character}' is not an alphabet.")