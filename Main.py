# Program to check if a student can enroll based on age  

def check_enrollment_age():  
    print("Welcome! Let's check if you can enroll in grade 10.")  
    try:  
        age = int(input("Please enter your age: "))  

        if 10 <= age <= 20:  
            print("You are eligible to enroll in Raj's class! 🎉")  
        elif age > 20:  
            print("Sorry, you are too old to enroll in Raj's class. 😔")  
        else:  
            print("Sorry, you are too young to enroll in Raj's class. 🌼")  

    except ValueError:  
        print("Oops! Please enter a valid number for your age. 😅")  

# Call the function to execute  
check_enrollment_age()