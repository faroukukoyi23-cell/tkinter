# Checkbutton And RadioButton Widgets
# 1. checkbutton: A checkbutton allows users to select or deselect an option independently.

# 2. RadioButton: A radiobutton allows users to select only one option from a group

# Example: checkbutton and radiobutton

import tkinter as tk
root = tk.Tk()
root.title("Selection Form")
root.geometry("400x300")

# checkbbutton
subscribe = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Subscribe to newsletter",
    variable=subscribe
).pack(pady=10)

# radiobutton
gender =tk.StringVar(value="Male")

tk.Radiobutton(
    root,
    text="Male",
    variable=gender,
    value="Male"
).pack()

tk.Radiobutton(
    root,
    text="Female",
    variable=gender,
    value="Female"
).pack()

# Display selections

def show_selection():
    print("Subscribed:", subscribe.get())
    print("Gender:", gender.get())

tk.Button(
    root,
    text="Submit",
    command=show_selection
).pack(pady=10)

root.mainloop()

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
