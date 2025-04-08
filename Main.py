import random  

def generate_random_password(length=8):  
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + '0123456789' + '!@#$%^&*()'  
    password = ''.join(random.choice(characters) for _ in range(length))  
    return ''.join(random.sample(password, len(password)))  

def generate_hints(password):  
    upper_case = ''.join(set([char for char in password if char.isupper()]))  
    lower_case = ''.join(set([char for char in password if char.islower()]))  
    digits = ''.join(set([char for char in password if char.isdigit()]))  
    special_characters = ''.join(set([char for char in password if not char.isalnum()]))  

    clues = []  
    if upper_case:  
        clues.append("uppercase letters: " + upper_case)  
    if lower_case:  
        clues.append("lowercase letters: " + lower_case)  
    if digits:  
        clues.append("numbers: " + digits)  
    if special_characters:  
        clues.append("special characters: " + special_characters)  
    
    min_digit = min(digits) if digits else None  
    max_digit = max(digits) if digits else None  

    specific_hints = []  
    if lower_case:  
        specific_hints.append("lowercase letters range from " + min(lower_case) + " to " + max(lower_case))  
    if upper_case:  
        specific_hints.append("uppercase letters range from " + min(upper_case) + " to " + max(upper_case))  
    if min_digit and max_digit:  
        specific_hints.append("numbers are between " + min_digit + " and " + max_digit)  

    return "The password contains " + ', '.join(clues) + ". " + ' and '.join(specific_hints) + "."  

def game():  
    print("Hello! Welcome to the Password Game. This is MEHER, the creator of this Password Game.")  
    name = input("May I know your name? ")  
    
    print("\nHello, " + name + "! Here are the rules:")  
    print("1. A random password will be generated.")  
    print("2. You will have 5 chances to guess the password.")  
    print("3. You will be given specific hints based on the generated password.")  
    print("4. If you guess the correct password, you win!")  
    print("5. If not, you'll see the correct password at the end.")  
    print("Hope you will enjoy the game!\n")  

    while True:  
        password = generate_random_password()  
        print("Try to guess the password!")  

        hints = generate_hints(password)  
        print("Hint: " + hints)  
        print("Hint: The password is " + str(len(password)) + " characters long.")  

        for attempt in range(5):  
            guess = input("Attempt " + str(attempt + 1) + "/5: ")  
            if guess == password:  
                print("\nCongo " + name + ", you've guessed the correct password: " + password + "!")  
                break  
            else:  
                print("Your guess is wrong.")  
        
        else:  
            print("The correct password was: " + password)  

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()  
        if play_again != 'yes':  
            print("Thanks for playing! Goodbye!")  
            break  

game()  