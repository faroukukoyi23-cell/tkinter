# Using Multiple Frames

# Frames become particulary useful when an application has multiple sections
# For example, you might have

# A header containing the application title.
# A content section information.
# A footer containing butons.

import tkinter as tk
root = tk.Tk()
root.title("Multiple Frames")
root.geometry("400x300")

header = tk.Frame(root, bg="navy", height=60)
header.pack(fill="x")

title = tk.Label(header, text="MY APPLICATION", bg="navy", fg="white")
title.pack(pady=20)

content =tk.Frame(root, bg="lightblue", height=150)
content.pack(fill="both", expand=True)

message = tk.Label(content, text="Welcome to the application", bg="lightblue")
message.pack(pady=40)

footer = tk.Frame(root, bg="lightgray", height=50)
footer.pack(fill="x")

button = tk.Button(footer, text="Exit", command=root.destroy)
button.pack(pady=10)

root.mainloop()
