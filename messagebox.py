# Messagebox Alerts And Notifications
# What is a Messagebox?
# A messagebx displays popup dialogs for messages, warnings, errors,

# Common  Messagebox methods

# showinfo() - Displays an information message.
# showwarning() - Displays a warning message.
# showerror() - displays an error message.
# askyesno() - Asks a yes/no question and returns True or False

import tkinter as tk
from tkinter import messagebox 

root = tk.Tk()
root.geometry("300x200")

def show_message():
    messagebox.showinfo("success", "Registration Successful")

def confirm_action():
    answer = messagebox.askyesno("confirm", "Do you want to continue?")
    if answer:
        messagebox.showinfo("Response", "You selected Yes")

tk.Button(root, text="Resgister", command=show_message).pack(pady=10)
tk.Button(root, text="Continue", command=confirm_action).pack(pady=10)      

root.mainloop()