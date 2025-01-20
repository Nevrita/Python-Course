# Assigning Different Variables
name = "Meher"
age = 12
is_student = True
weight = 30.6

# Printing Different Variables and their Data Type
print("Name :", name)
print("Data Type of Name is", type(name))

print("Age :", age)
print("Data Type of Age is", type(age))

print("Is Student :", is_student)
print("Data Type of is_student is", type(is_student))

print("Weight :", weight)
print("Data Type of weight is", type(weight))

# Type casting to convert the datatype of variables
print("\n After Type Casting....")  # \n means next line
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))