import tkinter as tk
from tkinter import messagebox 

root = tk.Tk()
root.title("Login System")
root.geometry("400x350")

header = tk.Frame(root, bg="white", height=60)
header.pack(fill="x")

title = tk.Label(header, text="USER LOGIN", bg="white", fg="white")
title.pack(pady=20)

content =tk.Frame(root, bg="darkgray", height=150)
content.pack(fill="both", expand=True)

message = tk.Label(content, text="Welcome to the art of slaughter", bg="lightblue")
message.pack(pady=40)

def greet():
    nickname = entry.get()
    passcode = int(entry.get())
    label.config(text=f"Welcome, {nickname}!")


tk.Label(content, text="Nickname: ").pack(pady=5)
tk.Label(content, text="Passcode: ").pack(pady=5)
entry = tk.Entry(content)
entry.pack(pady=5)

entry = tk.Entry(content)
entry.pack(pady=5)
tk.Button(content, text="Login", command=greet).pack(pady=50)

def show():
    if not nickname and not passcode:
        messagebox.showwarning("Warning", "Input your name")
def clear():
    tk.Button(content, text="Login", command=show).pack()
    tk.Button(content, text="Clear", command=clear).pack()

footer = tk.Frame(content, bg="lightgray", height=50)
footer.pack(fill="x")

root.mainloop()