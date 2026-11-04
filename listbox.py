# The listbox and Combobox widgets allows users to select items

# Listbox: Displays multiple items in a list.
# Combobox: Displays a dropdown list of options.

import tkinter as tk
root = tk.Tk()
root.title("Listbox Widget")
root.geometry("400x300")

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

listbox.insert(tk.END, "Python")
listbox.insert(tk.END, "Java")
listbox.insert(tk.END, "Javascript")
listbox.insert(tk.END, "C++")

# important methods we can use with Listbox
# listbox.insert(tk.END, "Python") -- Adds an item to the list
# listbox.get(index) -- Retrieves an item at a specific index
# listbox.curselection() -- Returns the index of the selected item
# listbox.delete(0, tk.END) -- Removes all items


# Retrieve a selected item

def show_selection():
    selected = listbox.curselection()

    if selected:
        item = listbox.get(selected)
        messagebox.showinfo("Selection", item)
    else:
        messagebox.showwarning("Warning", "Please select an item")

tk.Button(root, text="Submit", command=show_selection).pack()




root.mainloop()