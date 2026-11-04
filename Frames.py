# What are frames?
# A frame is a container used to group and organise widgets inside a window.
# Think of a frame as a box inside your application windows. You can place labels,
# buttons, entry fields, and other widgets inside that box.

# For example when creating a login form, you can put the username field, and
# login buttn inside one frame.


# For instance, you can use seperate frames for a login form,
# navigation butons, and a registration form.


# Why do we use frames?

# To organise widgets into seperate sections.
# To create cleaner application layouts.
# To manage groups of widgets independently.
# To make complex interfaces easier to structure.


# Creating A Frame
import tkinter as tk

root = tk.Tk()
root.title("Frame Widget")
root.geometry("400x300")

frame = tk.Frame(root, bg="lightblue", width=250, height=150)
frame.pack(pady=20)

root.mainloop()