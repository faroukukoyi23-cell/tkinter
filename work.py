import tkinter as tk

def welcome():
    label.config(text="Welcome carnage!")  
root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Change text")
label.pack()

button = tk.Button(root, text="Click", command=welcome)
button.pack()

root.mainloop()