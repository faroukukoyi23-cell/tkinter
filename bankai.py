import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Ichigo kukrosaki")
root.geometry("400x300")

tk.Label(root, text="Select Your Course: ").pack(pady=5)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

listbox.insert(tk.END, "Python")
listbox.insert(tk.END, "Java")
listbox.insert(tk.END, "Javascript")
listbox.insert(tk.END, "C++")

combo = ttk.Combobox(root, values = ["Beginner", "Intermediate", "Advanced", ], state="readonly")
combo.pack(pady=20)

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