import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Student Course Registration System")
root.geometry("600x650")
root.resizable(False, False)
root.config(bg="lightblue-grey")

header = tk.Frame(root, bg="navy", pady=20)
header.pack(fill="x")

tk.label(header, text="STUDENT REGISTRATION", font=("Arial", 20, "bold"), bg="navy", fg="white").pack()

tk.Label(header, text="Fill in your details to register for courses", font=("Arial", 11), bg="navy", fg="DCEBFA").pack(pady=5)

content = tk.Frame(root, bg="lightblue")
content.pack(fill="both",expand=True)

canvas = tk.Canvas(content, bg="lightblue")
