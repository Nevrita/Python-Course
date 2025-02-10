#Input the value of terms
n = int(input("Enter the value of terms: "))

sum = 0 #initialise
i = 1 #intialise
while i<=n: #loop will run from 1 to n
    sum = sum+i
    i = i+i

print("\nSum =", sum)