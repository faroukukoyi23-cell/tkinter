import tkinter as tk

def calculate():
    first_number = int(entry_1.get())
    second_number = int(entry_2.get())
    
    label.config(text=f"Answer: {first_number+second_number}!")

root = tk.Tk()
root.geometry("400x300")

tk.Label(root, text="Enter first number: ").pack(pady=5)
entry_1 = tk.Entry(root)
entry_1.pack()

tk.Label(root, text="Enter first number: ").pack(pady=5)
entry_2 = tk.Entry(root)
entry_2.pack()

tk.Button(root,text="Calculate", command=calculate).pack(pady=5)

label = tk.Label(root, text=" ")
label.pack(pady=5)

root.mainloop()