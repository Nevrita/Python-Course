def count_digits(number):  
    count = 0  
    while number > 0:  
        number //= 10  
        count += 1  
    return count  
if __name__ == "__main__":  
    num = int(input("Enter a number: "))  
    print(f"The number of digits in {num} is {count_digits(num)}.")