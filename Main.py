try:  
    age_input = input("Please enter your age: ")  
    
    age = int(age_input)  

    if age < 0:  
        raise ValueError("Age cannot be negative.")
    
    if age % 2 == 0:  
        print("The age " + str(age) + " is even.")  
    else:  
        print("The age " + str(age) + " is odd.")  

except ValueError as e:  
    print("Value error: " + str(e) + ". Please enter a valid integer for your age.")  

except Exception as e:  
    print("An unexpected error occurred: " + str(e))  

finally:  
    print("The age verification process has been completed successfully!!!")  