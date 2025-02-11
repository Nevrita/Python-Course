# Taking input  
input_number = input("Enter a number (you may use a dot or comma for decimals): ")  

# Replace commas with dots for uniformity  
input_number = input_number.replace(',', '.')  

try:  
    # Convert input to float and then to int for binary conversion  
    num = int(float(input_number))  
    
    if num < 0:  
        print("Negative numbers are not supported")  
    else:  
        binary = 0  
        multiplier = 1  

        while num > 0:  
            remainder = num % 2  
            binary += remainder * multiplier  
            num = num // 2  
            multiplier *= 10  

        print(f"The binary representation is: {binary}")  
except ValueError:  
    print("Invalid input. Please enter a valid number.")