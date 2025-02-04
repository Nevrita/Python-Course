print("Welcome to the Power Calculator!")  

# Taking user input  
base = float(input("Enter the base number: "))  
exponent = int(input("Enter the exponent: "))  

# Calculating the power  
result = int(base ** exponent)  

# Displaying the result  
print(f"{base} raised to the power of {exponent} is: {result}")