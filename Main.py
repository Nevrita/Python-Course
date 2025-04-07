def generate_odd_numbers(num):  
    return [x for x in range(num + 1) if x % 2 != 0]  

def get_capitalized_fruits():  
    fruits_input = input("Enter a list of fruits separated by commas: ")  

    fruits = []  
    current_fruit = ""  
    for charr in fruits_input:  
        if charr == ',':  
            if current_fruit: 
                fruits.append(current_fruit)  
            current_fruit = ""  
        else:  
            current_fruit += charr  
            
    if current_fruit:
        fruits.append(current_fruit)  

    return [fruit.capitalize() for fruit in fruits]  

num = int(input("Enter a maximum number to generate odd numbers: "))  
odd_numbers = generate_odd_numbers(num)  

capitalized_fruits = get_capitalized_fruits()  
  
print("List of odd numbers:", odd_numbers)  
print("List of capitalized fruits:", capitalized_fruits)  