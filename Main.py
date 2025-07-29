import tkinter as tk
import random

def play(choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    result = ''

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == 'rock' and computer_choice == 'scissors') or \
         (choice == 'scissors' and computer_choice == 'paper') or \
         (choice == 'paper' and computer_choice == 'rock'):
        result = 'You Win!'
    else:
        result = 'Computer Wins!'

    result_label.config(text=f'Your choice: {choice}\nComputer: {computer_choice}\n{result}')

# Create main window with sky blue background
root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("400x400")
root.configure(bg='skyblue')

# Buttons for choices with background color matching window
tk.Button(root, text='Rock', command=lambda: play('rock'), bg='white').pack(pady=10)
tk.Button(root, text='Paper', command=lambda: play('paper'), bg='white').pack(pady=10)
tk.Button(root, text='Scissors', command=lambda: play('scissors'), bg='white').pack(pady=10)

# Label to display result
result_label = tk.Label(root, text='', font=('Arial', 14), bg='skyblue')
result_label.pack(pady=20)

root.mainloop()