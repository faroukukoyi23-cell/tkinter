# Combobox Widget
# A Combobox displays a dropdown list from which users can select an option.

#It is providedby tkinter.ttk, so you must ttk
import tkinter as tk
from tkinter import ttk
from import tkinter import ttk, messagebox

root = tk.Tk()
root.title("Combo Widget")
root.geometry("300x200")

combo = ttk.Combobox(root, values = ["Python", "Java", "Javascript", "C++"], state="readonly")
combo.pack(pady=20)

# Additionl methods

# comb.get() -- Retrieves the selected value
# combo.set("Python") -- Sets the displayed value

# RETRIEVING A COMBO SELECTION

def show_selection():
    selected = combo.get()

    if selected:
        messagebox.showinfo("Selection", selected)
    else:
        messagebox.showwarning("Warning", "Please select a language")

def clear():
    combo.set("")

tk.Button(root, text="Submit", command=show_selection).pack()
tk.Button(root, text="Clear", command=clear).pack()

root.mainloop()

# Build a course selection form with the followinng features:
# 1. A label displaying select your course.
# 2. A listbox containing Python, java, javascript, and c++.
# 3. A combobox containing beginner, intermediate, and Advanced.
# 4. A submit button that displays the selected course and level
# 5. A clear button that clears the course selection and resets the level
# note: For the listbox, use curseleecction() to retrieve the selected course.
# For the combobox, use get() to retrieve the selected level.