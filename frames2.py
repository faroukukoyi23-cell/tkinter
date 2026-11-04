# Placing Widgets Inside A frame

# This iss one of the most important things to understand about frames.
# Instead of placing every widget directly inside the main window, youu can place related widgets inside a frame.

import tkinter as tk
app = tk.Tk()
app.title("BAKA")
app.geometry("400x300")

frame = tk.Frame(app, bg="lightblue", width=250, height=150, padx=20, pady=20)
frame.pack(pady=30)
frame.pack_propagate(False)

label = tk.Label(frame, text="Welcome to tkinter")
label.pack()

button = tk.Button(frame, text="Click Me")

button.pack(pady=10)


app.mainloop()