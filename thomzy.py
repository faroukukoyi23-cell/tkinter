import tkinter as tk

# What are tkinter variables?
# Tkinter variables store values that can be linked to widgets and updated dynamically

# Types of tkinter variables

# StringVar(): Stores text values.
# IntVar(): Stores integer values.
# DoubleVar(): Stores decimal Values.
# BooleanVar(): Stores boolean values (True or False).

# Example: Using StringVar()

root = tk.Tk
root.geometry("400x250")

name = tk.StringVar()  # Creates a text variable

entry = tk.Entry(root, textvariable=name)   #Link variable to entry
entry.pack(pady=10)

label = tk.Label(root,text="")
label.pack(pady=10)

def display_name():
    label.config(text=name.get())   # Retrieve the variable's value

tk.Button(root,text="Display Name", command=display_name).pack()

root.mainloop()

name.set("Larry")  # Set's the variable value
print(name.get())  # Display the current value