import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window size
root.geometry('400x400')

# Set window title
root.title('Length Converter App')

# Set background color to sky blue
root.configure(bg='#87ceeb')

# Create and place a label for instructions
instruction_label = tk.Label(root, text='Enter length in inches:', bg='#87ceeb', fg='#333333', font=('Arial', 12))
instruction_label.pack(pady=10)

# Entry widget for user input
inch_entry = tk.Entry(root, width=20, font=('Arial', 12))
inch_entry.pack(pady=5)

# Label to display result
result_label = tk.Label(root, text='', bg='#87ceeb', fg='#555555', font=('Arial', 12))
result_label.pack(pady=10)

# Function to convert inches to centimeters
def convert():
    try:
        inches = float(inch_entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f'{inches} inches is {centimeters:.2f} centimeters.')
    except ValueError:
        result_label.config(text='Please enter a valid number.')

# Convert button
convert_button = tk.Button(root, text='Convert', command=convert, bg='#ff7f50', fg='white', font=('Arial', 12))
convert_button.pack(pady=5)

# Run the application
root.mainloop()