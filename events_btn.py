import tkinter as tk
# What are Events

# Events are user actions, such as clicking a button or
# preesing a key that trigger a response in an application

# The command parameter

# The command parameter specifies the function to execute when  a button is clicked

# Example Button command
def greet():
    label.config(text="Welcome To Tkinter!")  # Update the label text

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Click the button")
label.pack()

button = tk.Button(root, text="Click Me", command=greet)
button.pack()

root.mainloop()