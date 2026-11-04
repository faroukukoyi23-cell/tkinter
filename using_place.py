import tkinter as tk
app =tk.Tk()
app.title("Using Place")
app.geometry("400x300")

tk.Label(app, text="Welcome").place(x=150, y=50)
tk.Button(app, text="Login").place(x=160, y=100)

app.mainloop()
# create a login interace, containing,
# 1. username and an ntry field
# 2. password and an entry field
# 3. login button
# 4. use grid to arrange the login button
