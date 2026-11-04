
import tkinter as tk
from tkinter import ttk, messagebox

# ==================================
# MAIN WINDOW
# ==================================

root = tk.Tk()
root.title("Student Course Registration System")
root.geometry("850x850")
root.minsize(650, 650)
root.resizable(True, True)
root.configure(bg="#F1F5F9")

# Store registered students
registration_data = []

# Colour scheme
NAVY = "#163A5F"
BLUE = "#2563EB"
LIGHT_BLUE = "#F1F5F9"
WHITE = "#FFFFFF"
DARK = "#1E293B"
GREEN = "#0F766E"


# ==================================
# HEADER
# ==================================

header = tk.Frame(root, bg=NAVY, pady=20)
header.pack(fill="x")

tk.Label(
    header,
    text="STUDENT COURSE REGISTRATION",
    font=("Arial", 20, "bold"),
    bg=NAVY,
    fg=WHITE
).pack()

tk.Label(
    header,
    text="Fill in your details to register for courses",
    font=("Arial", 11),
    bg=NAVY,
    fg="#DCEBFA"
).pack(pady=5)


# ==================================
# SCROLLABLE FORM AREA
# ==================================

container = tk.Frame(root, bg=LIGHT_BLUE)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(
    container,
    bg=LIGHT_BLUE,
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    container,
    orient="vertical",
    command=canvas.yview
)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

main_frame = tk.Frame(canvas, bg=LIGHT_BLUE, padx=25, pady=20)

window_id = canvas.create_window(
    (0, 0),
    window=main_frame,
    anchor="nw"
)


def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


def resize_form(event):
    canvas.itemconfigure(window_id, width=event.width)


main_frame.bind("<Configure>", update_scroll_region)
canvas.bind("<Configure>", resize_form)


# ==================================
# STUDENT INFORMATION
# ==================================

personal_frame = tk.LabelFrame(
    main_frame,
    text=" Student Information ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=NAVY,
    padx=15,
    pady=15
)

personal_frame.pack(fill="x", pady=10)

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()


def create_field(parent, label_text, variable, row):
    tk.Label(
        parent,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(row=row, column=0, sticky="w", pady=10)

    entry = tk.Entry(
        parent,
        textvariable=variable,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )

    entry.grid(
        row=row,
        column=1,
        sticky="ew",
        padx=15,
        pady=10,
        ipady=6
    )


personal_frame.columnconfigure(1, weight=1)

create_field(personal_frame, "Full Name:", name_var, 0)
create_field(personal_frame, "Email Address:", email_var, 1)
create_field(personal_frame, "Phone Number:", phone_var, 2)


# ==================================
# COURSE SELECTION
# ==================================

course_frame = tk.LabelFrame(
    main_frame,
    text=" Course Selection ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=NAVY,
    padx=15,
    pady=15
)

course_frame.pack(fill="x", pady=10)

tk.Label(
    course_frame,
    text="Select the courses you want to study:",
    font=("Arial", 10),
    bg=WHITE,
    fg=DARK
).pack(anchor="w")

course_list = tk.Listbox(
    course_frame,
    selectmode=tk.MULTIPLE,
    height=6,
    font=("Arial", 11),
    bg="#F8FAFC",
    fg=DARK,
    selectbackground=BLUE,
    relief="solid",
    bd=1,
    exportselection=False
)

courses = [
    "Python Programming",
    "Java Programming",
    "Web Development",
    "Database Management",
    "Graphic Design",
    "Cybersecurity"
]

for course in courses:
    course_list.insert(tk.END, course)

course_list.pack(fill="x", pady=10)


# ==================================
# LEARNING MODE
# ==================================

mode_frame = tk.LabelFrame(
    main_frame,
    text=" Learning Mode ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=NAVY,
    padx=15,
    pady=15
)

mode_frame.pack(fill="x", pady=10)

mode_var = tk.StringVar(value="")

for mode in ["Physical", "Online", "Hybrid"]:
    tk.Radiobutton(
        mode_frame,
        text=mode,
        variable=mode_var,
        value=mode,
        font=("Arial", 10),
        bg=WHITE,
        fg=DARK,
        activebackground=WHITE
    ).pack(anchor="w", pady=3)


# ==================================
# EXPERIENCE LEVEL
# ==================================

experience_frame = tk.LabelFrame(
    main_frame,
    text=" Experience Level ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=NAVY,
    padx=15,
    pady=15
)

experience_frame.pack(fill="x", pady=10)

experience_var = tk.StringVar()

experience_box = ttk.Combobox(
    experience_frame,
    textvariable=experience_var,
    values=["Beginner", "Intermediate", "Advanced"],
    state="readonly",
    font=("Arial", 11)
)

experience_box.pack(fill="x", pady=5)


# ==================================
# ADDITIONAL INFORMATION
# ==================================

info_frame = tk.LabelFrame(
    main_frame,
    text=" Additional Information ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=NAVY,
    padx=15,
    pady=15
)

info_frame.pack(fill="x", pady=10)

info_text = tk.Text(
    info_frame,
    height=5,
    font=("Arial", 10),
    bg="#F8FAFC",
    fg=DARK,
    relief="solid",
    bd=1
)

info_text.pack(fill="x")


# ==================================
# TERMS AND CONDITIONS
# ==================================

terms_var = tk.BooleanVar()

terms_check = tk.Checkbutton(
    main_frame,
    text="I agree to the terms and conditions.",
    variable=terms_var,
    font=("Arial", 10),
    bg=LIGHT_BLUE,
    fg=DARK,
    activebackground=LIGHT_BLUE
)

terms_check.pack(anchor="w", pady=15)


# ==================================
# SUBMIT REGISTRATION FUNCTION
# ==================================

def register_student():

    name = name_var.get().strip()
    email = email_var.get().strip()
    phone = phone_var.get().strip()

    selected_indices = course_list.curselection()

    selected_courses = [
        course_list.get(index)
        for index in selected_indices
    ]

    mode = mode_var.get()
    experience = experience_var.get()
    additional_info = info_text.get("1.0", tk.END).strip()

    # VALIDATION

    if not name or not email or not phone:
        messagebox.showerror(
            "Missing Information",
            "Please fill in your name, email and phone number."
        )
        return

    if "@" not in email or "." not in email.split("@")[-1]:
        messagebox.showerror(
            "Invalid Email",
            "Please enter a valid email address."
        )
        return

    if not phone.replace("+", "").replace("-", "").replace(" ", "").isdigit():
        messagebox.showerror(
            "Invalid Phone Number",
            "Please enter a valid phone number."
        )
        return

    if not selected_courses:
        messagebox.showerror(
            "Course Required",
            "Please select at least one course."
        )
        return

    if not mode:
        messagebox.showerror(
            "Learning Mode Required",
            "Please select a learning mode."
        )
        return

    if not experience:
        messagebox.showerror(
            "Experience Required",
            "Please select your experience level."
        )
        return

    if not terms_var.get():
        messagebox.showerror(
            "Terms and Conditions",
            "Please agree to the terms and conditions."
        )
        return

    # SAVE REGISTRATION

    student = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Courses": selected_courses,
        "Learning Mode": mode,
        "Experience Level": experience,
        "Additional Information": additional_info
    }

    registration_data.append(student)

    messagebox.showinfo(
        "Registration Successful",
        f"Congratulations, {name}!\n\n"
        "Your registration has been submitted successfully."
    )

    clear_form(confirm=False)


# ==================================
# CLEAR FORM FUNCTION
# ==================================

def clear_form(confirm=True):

    if confirm:
        answer = messagebox.askyesno(
            "Clear Form",
            "Are you sure you want to clear the form?"
        )

        if not answer:
            return

    name_var.set("")
    email_var.set("")
    phone_var.set("")

    course_list.selection_clear(0, tk.END)

    mode_var.set("")
    experience_var.set("")

    info_text.delete("1.0", tk.END)

    terms_var.set(False)


# ==================================
# VIEW REGISTRATION FUNCTION
# ==================================

def view_registration():

    if not registration_data:
        messagebox.showinfo(
            "No Registrations",
            "No student has registered yet."
        )
        return

    view_window = tk.Toplevel(root)
    view_window.title("Registered Students")
    view_window.geometry("650x550")
    view_window.minsize(450, 350)
    view_window.configure(bg=LIGHT_BLUE)

    tk.Label(
        view_window,
        text="REGISTERED STUDENTS",
        font=("Arial", 17, "bold"),
        bg=NAVY,
        fg=WHITE,
        pady=15
    ).pack(fill="x")

    output = tk.Text(
        view_window,
        font=("Arial", 11),
        bg=WHITE,
        fg=DARK,
        padx=15,
        pady=15,
        wrap="word"
    )

    output.pack(fill="both", expand=True, padx=15, pady=15)

    for number, student in enumerate(registration_data, start=1):

        output.insert(
            tk.END,
            f"REGISTRATION {number}\n"
        )

        output.insert(tk.END, "-" * 40 + "\n")

        for key, value in student.items():

            if isinstance(value, list):
                value = ", ".join(value)

            output.insert(
                tk.END,
                f"{key}: {value}\n"
            )

        output.insert(tk.END, "\n\n")

    output.config(state="disabled")


# ==================================
# BUTTONS
# ==================================

button_frame = tk.Frame(
    main_frame,
    bg=LIGHT_BLUE
)

button_frame.pack(pady=20)

submit_button = tk.Button(
    button_frame,
    text="SUBMIT REGISTRATION",
    command=register_student,
    font=("Arial", 11, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    activeforeground=WHITE,
    padx=18,
    pady=12,
    relief="flat",
    cursor="hand2"
)

submit_button.pack(pady=7, fill="x")

clear_button = tk.Button(
    button_frame,
    text="CLEAR FORM",
    command=clear_form,
    font=("Arial", 10, "bold"),
    bg="#E2E8F0",
    fg=DARK,
    padx=18,
    pady=10,
    relief="flat",
    cursor="hand2"
)

clear_button.pack(side="left", padx=5)

view_button = tk.Button(
    button_frame,
    text="VIEW REGISTRATIONS",
    command=view_registration,
    font=("Arial", 10, "bold"),
    bg=GREEN,
    fg=WHITE,
    padx=18,
    pady=10,
    relief="flat",
    cursor="hand2"
)

view_button.pack(side="left", padx=5)


# ==================================
# START APPLICATION
# ==================================

root.mainloop()
