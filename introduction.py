# What is a tkinter?
# thinkter is a standard GUI (Graphical User Interface) library, Desktop applications for python. It provides a fast and easy way to create GUI
# applications. This library is included with most python installations, so you don't need to install anything extra to use it.
import tkinter as tk # this imports the tkinter library.
root = tk.Tk() # this creates the main application window.
# create the main application window.
root.title("My First App") # sets the window title of the main application window 
root.geometry("400x300") # it sets the size of the window.
root.mainloop() # it starts the tkinter eventt loop, alllowng the the window to be displayed and respond to user interactions.