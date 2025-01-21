# Take Marks As Input From User
print("Enter Marks Obtaines in 4 Subjects: ")
Math = int(input("Maths: "))
English = int(input("English: "))
Science = int(input("Science: "))
Arts_and_Crafts = int(input("Arts and Crafts: "))

# Let's calculate the percentage of marks
sum = Math+English+Science+Arts_and_Crafts
print("Sum of Math, English, Science and Art")

perc = (sum/400)*100

print(end = "Percentage Mark = ")
print(perc)