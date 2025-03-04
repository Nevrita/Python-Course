try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is : ", result)

except ZeroDivisionError:
    print("Division by zero is not not allowed")
except ValueError:
    print("Please enter numerial value")
except NameError as ex:
    print("The exception is ",ex)

except:
    print("Some errror occurred")
finally:
    print("I will execute no matter what happens")