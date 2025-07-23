import tkinter as tk

# Create main window
window = tk.Tk()
window.geometry("400x400")
window.title("Age Calculator App")

# Labels and entries for input
tk.Label(window, text="Age:").grid(row=0, column=0, padx=10, pady=10)
age_entry = tk.Entry(window)
age_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Time (years):").grid(row=1, column=0, padx=10, pady=10)
time_entry = tk.Entry(window)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Rate of interest (%):").grid(row=2, column=0, padx=10, pady=10)
interest_entry = tk.Entry(window)
interest_entry.grid(row=2, column=1, padx=10, pady=10)

# Label to display result
result_label = tk.Label(window, text="Simple interest will be shown here")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Function to calculate simple interest
def calculate_interest():
    try:
        p = float(age_entry.get())
        t = float(time_entry.get())
        r = float(interest_entry.get())
        simple_interest = (p * t * r) / 100
        result_label.config(text=f"Simple Interest: {simple_interest}")
    except ValueError:
        result_label.config(text="Please enter valid numerical values.")

# Button to trigger calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()