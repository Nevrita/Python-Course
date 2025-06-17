import tkinter as tk

# Create main window
window = tk.Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")
window.configure(bg="#d0efff")

# Function to calculate product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"The product is: {product}")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers.")

# Description label
desc_label = tk.Label(window, text="This application calculates the product of two numbers.", bg="#d0efff")
desc_label.pack(pady=10)

# Ask for first number
label1 = tk.Label(window, text="Enter first number:", bg="#d0efff")
label1.pack()

# Entry for first number
entry1 = tk.Entry(window, bg="#ffffff")
entry1.pack()

# Ask for second number
label2 = tk.Label(window, text="Enter second number:", bg="#d0efff")
label2.pack()

# Entry for second number
entry2 = tk.Entry(window, bg="#ffffff")
entry2.pack()

# Button to start calculation
calc_button = tk.Button(window, text="Calculate Product", command=calculate_product, bg="#87CEFA")
calc_button.pack(pady=10)

# Text box to display results
result_text = tk.Text(window, height=2, width=30, bg="#E0FFFF")
result_text.pack()

# Run the application
window.mainloop()