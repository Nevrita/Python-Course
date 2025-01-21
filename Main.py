import math  

def calculate_square_root():  
    try:  
        number = float(input("Enter a number to find its square root: "))  
        if number < 0:  
            print("Sorry, square root of a negative number is not defined.")  
        else:  
            square_root = math.sqrt(number)  
            # Check if the input number is an integer  
            if number.is_integer():  
                number = int(number)  
            # Print the square root as an integer if it is a whole number  
            if square_root.is_integer():  
                square_root = int(square_root)  
            print(f"The square root of {number} is {square_root}")  
    except ValueError:  
        print("Invalid input! Please enter a valid number.")  

if __name__ == "__main__":  
    calculate_square_root()