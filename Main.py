def get_range():  
    start = int(input("Enter the starting number: "))  
    end = int(input("Enter the ending number: "))  
    return start, end  

def calculate_squares(start, end):  
    return [i ** 2 for i in range(start, end + 1)]  

def filter_odd_squares(squares):  
    odd_squares = []  
    for square in squares:  
        if square % 2 != 0:  
            odd_squares.append(square)  
    return odd_squares  
  
start, end = get_range()  
squares = calculate_squares(start, end)  
odd_squares = filter_odd_squares(squares)  

print("Odd squares:", odd_squares)