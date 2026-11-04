import tkinter as tk
root = tk.Tk()
root.title("Carnage Freestyle")
root.geometry("400x300")

label = tk.Label(root, text = "Wagwan, Carnage Vortex")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text = "Submitted")
button.pack()
 
root.configure(bg = "darkblue")

root.mainloop()