# What are widget?
# Widgets are GUI elements used to bulid and interact with a tkinter application, in other words, they are building blocks
# Caommon tkinter widget: 
# 1. Label
# 2. Button
# 3. Entry
# 4. Text
# 5. Frame

# Checkbutton - A check box that allos users to select and diselect an option.
# Radiobutton - A buuton that allow users to select option from a group of option.

import tkinter as tk
root = tk.Tk()
root.title("Tkinter Widget")
root.geometry("400x300")

label = tk.Label(root, text = "Hello, Carnage") # create a label
label.pack () # adds label to the window

entry = tk.Entry(root) # create and input field
entry.pack() # adds the input field to the window

button = tk.Button(root, text = "Submit") # creates a button
button.pack() # adds teh button tto the window

root.mainloop()

# Assignment
# Creaate window containig your fullname and entry field for entring your age and button name submit