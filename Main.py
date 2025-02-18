import turtle  

# Get user input  
name = turtle.textinput("Input", "Enter your name:")  

# Set up turtle  
turtle.bgcolor("dark blue")  
turtle.color("white")  
turtle.speed(1)  

# Draw a larger square  
turtle.penup()  
turtle.goto(-150, 100)  # Move to starting position to center the square  
turtle.pendown()  
for _ in range(4):  
    turtle.forward(300)  # Increased size for the square  
    turtle.right(90)  

# Move to center to write welcome message  
turtle.penup()  
turtle.goto(0, 20)  # Centered in the square  
turtle.pendown()  
turtle.color("white")  
welcome_message = f"Welcome {name}" if name else "Welcome User"  
turtle.write(welcome_message, align="center", font=("Arial", 18, "normal"))  

# Move below the square to write the project message  
turtle.penup()  
turtle.goto(0, -50)  # Position below the square  
turtle.pendown()  
turtle.write("The project is made by \n Meher Nigar Hridy", align="center", font=("Arial", 14, "bold"))  

# Hide turtle and finish  
turtle.hideturtle()  
turtle.done()