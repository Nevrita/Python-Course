test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}  

print("The original dictionary : " + str(test_dict))  

K = int(input("Enter the value to check the frequency: "))  

result = 0  
for key in test_dict:  
    if test_dict[key] == K:  
        result += 1 

print("Frequency of", K, "is :", result)  