def check_clothing(temperature):  
    if temperature > 20:  
        return "It's warm enough for light clothes!"  
    elif 15 < temperature <= 20:  
        return "You might want a light jacket, but light clothes should be fine."  
    elif 10 < temperature <= 15:  
        return "It's getting a bit chilly; a sweater might be a good idea."  
    else:  
        return "It's too cold for light clothes. Better wear a jacket!"  

# Example usage  
current_temperature = float(input("Enter the current temperature in °C: "))  
suggestion = check_clothing(current_temperature)  
print(suggestion)