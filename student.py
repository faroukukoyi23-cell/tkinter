import tkinter as tk

root = tk.Tk()
root.title("Student Registration System")
root.geometry("500x400")


def register():
    name = entry.get()
    age = int(entry_1.get())
    email = entry_2.get()
    department = entry_3.get()

    label4.config(
        text=f"{name}, {age}, {email}, {department}"
    )


label = tk.Label(root, text="Name: ")
label.grid(row=0, column=0, pady=5)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

label_1 = tk.Label(root, text="Age: ")
label_1.grid(row=2, column=0, pady=6)

entry_1 = tk.Entry(root)
entry_1.grid(row=2, column=1)

label_2 = tk.Label(root, text="Email: ")
label_2.grid(row=4, column=0, pady=7)

entry_2 = tk.Entry(root)
entry_2.grid(row=4, column=1)

label_3 = tk.Label(root, text="Department: ")
label_3.grid(row=6, column=0, pady=8)

entry_3 = tk.Entry(root)
entry_3.grid(row=6, column=1)

button = tk.Button(root, text="Register", command=register)
button.grid(row=8, column=1, pady=10)

label4 = tk.Label(root, text="")
label4.grid(row=10, column=4,)