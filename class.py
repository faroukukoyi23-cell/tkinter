import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def greet():
    name = entry.get()

    if not name:
        messagebox.showwarning("Warning", "You didn't put a name")
    else:
        answer = messagebox.askyesno("confirm", "Nice name")
    if answer:
            messagebox.showinfo("Success", "Name confirmed")

tk.Label(root, text="Enter your name: ").pack(pady=5)

entry = tk.Entry(root) 
entry.pack(pady=5)

tk.Button(root, text="Submit", command=greet).pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()