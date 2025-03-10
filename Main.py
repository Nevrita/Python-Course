import random
playing = True
number = str(random.randint(10,20))

print("I will generate a number from 10 to 20, and you will have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!!!")
while playing:
    guess = input("Give me your BEST GUESS!!! \n")
    if number == guess:
        print("You have WON the Game!!!")
        print("The number was", number)
        break

    else:
        print("Your guess isn't quite right, try again. \n")
