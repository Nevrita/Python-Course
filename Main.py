import math  

def square_perimeter(side):  
    """Calculate the perimeter of a square."""  
    return 4 * side  

def rectangle_perimeter(length, width):  
    """Calculate the perimeter of a rectangle."""  
    return 2 * (length + width)  

def circle_circumference(radius):  
    """Calculate the circumference of a circle."""  
    return 2 * math.pi * radius  

def clear_screen():  
    """Clear the console screen for better interface."""  
    import os  
    os.system('cls' if os.name == 'nt' else 'clear')  

def main():  
    while True:  
        clear_screen()  
        print("Shape Perimeter Calculator")  
        print("1. Square")  
        print("2. Rectangle")  
        print("3. Circle")  
        print("4. Exit")  
        
        choice = input("Please choose an option (1-4): ")  

        if choice == '1':  
            side = float(input("Enter side length of the square: "))  
            print(f"The perimeter of the square is: {square_perimeter(side)}")  
        
        elif choice == '2':  
            length = float(input("Enter length of the rectangle: "))  
            width = float(input("Enter width of the rectangle: "))  
            print(f"The perimeter of the rectangle is: {rectangle_perimeter(length, width)}")  
        
        elif choice == '3':  
            radius = float(input("Enter radius of the circle: "))  
            print(f"The circumference of the circle is: {circle_circumference(radius)}")  
        
        elif choice == '4':  
            print("Thank you for using the calculator. Goodbye!")  
            break  
        
        else:  
            print("Invalid choice! Please select a valid option.")  
        
        input("Press Enter to continue...")  

if __name__ == "__main__":  
    main()