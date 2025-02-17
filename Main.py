n = int(input("Enter the height of the triangle: "))  

for i in range(1, n + 1):  
    print(' ' * (n - i) + '*' * i)