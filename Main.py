import tkinter as tk

def check_strength():
    pwd = entry.get()
    length = len(pwd)
    if length <= 5:
        color, text = "red", "Weak"
    elif 6 <= length <= 8:
        color, text = "orange", "Medium"
    elif 9 <= length <= 12:
        color, text = "lightgreen", "Strong"
    else:
        color, text = "darkgreen", "Very Strong"

    result.config(text=text, fg=color)

# Create main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#E6E6FA")  # Lavender color

# Label
label = tk.Label(root, text="Enter Password:", bg="#E6E6FA", font=("Arial", 14))
label.pack(pady=20)

# Entry widget
entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

# Button to check password strength
btn = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
btn.pack(pady=10)

# Label to display result
result = tk.Label(root, text="", bg="#E6E6FA", font=("Arial", 16, "bold"))
result.pack(pady=20)

# Run the app
root.mainloop()