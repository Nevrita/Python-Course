import tkinter as tk
import datetime

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = datetime.date.today()
        birth_date = datetime.date(year, month, day)

        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        message = f"Hello, {name}! Your present age is {age} years."
        result_label.config(text=message)
    except ValueError:
        # Using the existing messagebox from tkinter
        tk.messagebox.showerror("Invalid input", "Please enter valid numbers for date, month, and year.")
    except Exception as e:
        tk.messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.config(background="#f0f0f0")  # Light gray background

# Name input
name_label = tk.Label(root, text="Name:", bg="#f0f0f0")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Date of Birth input
dob_label = tk.Label(root, text="Date of Birth:", bg="#f0f0f0")
dob_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

dob_frame = tk.Frame(root, bg="#f0f0f0")
dob_frame.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Day input
day_label = tk.Label(dob_frame, text="Day:", bg="#f0f0f0")
day_label.grid(row=0, column=0, padx=5)
day_entry = tk.Entry(dob_frame, width=5)
day_entry.grid(row=0, column=1, padx=5)

# Month input
month_label = tk.Label(dob_frame, text="Month:", bg="#f0f0f0")
month_label.grid(row=0, column=2, padx=5)
month_entry = tk.Entry(dob_frame, width=5)
month_entry.grid(row=0, column=3, padx=5)

# Year input
year_label = tk.Label(dob_frame, text="Year:", bg="#f0f0f0")
year_label.grid(row=0, column=4, padx=5)
year_entry = tk.Entry(dob_frame, width=8)
year_entry.grid(row=0, column=5, padx=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="#4CAF50", fg="white")
calc_button.grid(row=2, column=0, columnspan=2, pady=20)

# Result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()