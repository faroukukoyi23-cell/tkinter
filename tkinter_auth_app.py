import hashlib
import hmac
import os
import re
import sqlite3
import tkinter as tk
from tkinter import messagebox

APP_TITLE = "Nova | Desktop Account"
DB_NAME = "users.db"
BG = "#0B1220"
PANEL = "#121C2E"
FIELD = "#1B2940"
TEXT = "#F2F5FA"
MUTED = "#9AA9BF"
ACCENT = "#6D8DFF"
ACCENT_HOVER = "#5578F0"
SUCCESS = "#36C98F"
DANGER = "#FF6B7A"


def hash_password(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    """Return (salt, derived password hash) using PBKDF2."""
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 200_000
    )
    return salt, digest


class AuthApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("900x600")
        self.minsize(760, 520)
        self.configure(bg=BG)

        self.current_user = None
        self._init_db()

        # A single container holds one screen at a time.
        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True)

        self.show_login()

    def _init_db(self):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL COLLATE NOCASE UNIQUE,
                    email TEXT NOT NULL COLLATE NOCASE UNIQUE,
                    salt BLOB NOT NULL,
                    password_hash BLOB NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def _clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def _center_card(self, width=430):
        """Create a centered-looking card using a grid layout."""
        wrapper = tk.Frame(self.container, bg=BG)
        wrapper.pack(fill="both", expand=True)
        wrapper.grid_rowconfigure(0, weight=1)
        wrapper.grid_columnconfigure(0, weight=1)

        card = tk.Frame(wrapper, bg=PANEL, padx=36, pady=32, width=width)
        card.grid(row=0, column=0, padx=20, pady=20)
        card.grid_propagate(False)
        return card

    def _label(self, parent, text, size=11, color=TEXT, bold=False):
        return tk.Label(
            parent,
            text=text,
            bg=PANEL,
            fg=color,
            font=("Segoe UI", size, "bold" if bold else "normal"),
            anchor="w",
        )

    def _entry(self, parent, placeholder="", show=None):
        entry = tk.Entry(
            parent,
            bg=FIELD,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            bd=0,
            font=("Segoe UI", 11),
            show=show or "",
            highlightthickness=1,
            highlightbackground=FIELD,
            highlightcolor=ACCENT,
        )
        entry.insert(0, placeholder)
        entry.pack(fill="x", ipady=11, pady=(6, 15))
        return entry

    def _button(self, parent, text, command, secondary=False):
        bg = FIELD if secondary else ACCENT
        active = "#263853" if secondary else ACCENT_HOVER
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=TEXT,
            activebackground=active,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            padx=14,
            pady=11,
        )
        button.pack(fill="x", pady=(4, 8))
        return button

    def _link(self, parent, text, command):
        link = tk.Button(
            parent,
            text=text,
            command=command,
            bg=PANEL,
            fg=ACCENT,
            activebackground=PANEL,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10),
        )
        link.pack(pady=(6, 0))
        return link

    def show_login(self):
        self._clear_screen()
        card = self._center_card()

        self._label(card, "N O V A", 12, ACCENT, True).pack(anchor="w")
        self._label(card, "Welcome back", 24, TEXT, True).pack(
            anchor="w", pady=(16, 4)
        )
        self._label(card, "Log in to continue to your workspace.", 10, MUTED).pack(
            anchor="w", pady=(0, 24)
        )

        self._label(card, "Username or email").pack(anchor="w")
        self.login_identity = self._entry(card)
        self._label(card, "Password").pack(anchor="w")
        self.login_password = self._entry(card, show="•")

        self._button(card, "Log in", self.login)
        self._link(card, "New here? Create an account", self.show_signup)
        self.login_identity.focus_set()

        self.bind("<Return>", lambda event: self.login())

    def show_signup(self):
        self._clear_screen()
        card = self._center_card()

        self._label(card, "N O V A", 12, ACCENT, True).pack(anchor="w")
        self._label(card, "Create your account", 23, TEXT, True).pack(
            anchor="w", pady=(12, 3)
        )
        self._label(card, "A few details and you're ready to go.", 10, MUTED).pack(
            anchor="w", pady=(0, 18)
        )

        self._label(card, "Username").pack(anchor="w")
        self.signup_username = self._entry(card)
        self._label(card, "Email address").pack(anchor="w")
        self.signup_email = self._entry(card)
        self._label(card, "Password (at least 8 characters)").pack(anchor="w")
        self.signup_password = self._entry(card, show="•")
        self._label(card, "Confirm password").pack(anchor="w")
        self.signup_confirm = self._entry(card, show="•")

        self._button(card, "Create account", self.signup)
        self._link(card, "Already registered? Log in", self.show_login)

        # The card has a fixed height, so allow a little more room for this form.
        card.configure(height=560)
        self.bind("<Return>", lambda event: self.signup())

    def signup(self):
        username = self.signup_username.get().strip()
        email = self.signup_email.get().strip().lower()
        password = self.signup_password.get()
        confirm = self.signup_confirm.get()

        if not username or not email or not password or not confirm:
            messagebox.showwarning("Missing information", "Please fill in every field.")
            return
        if len(username) < 3 or not re.fullmatch(r"[A-Za-z0-9_.-]+", username):
            messagebox.showwarning(
                "Invalid username",
                "Use at least 3 characters: letters, numbers, dots, _ or -.",
            )
            return
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            messagebox.showwarning("Invalid email", "Enter a valid email address.")
            return
        if len(password) < 8:
            messagebox.showwarning(
                "Weak password", "Your password must be at least 8 characters."
            )
            return
        if password != confirm:
            messagebox.showwarning("Password mismatch", "The passwords do not match.")
            return

        salt, digest = hash_password(password)
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute(
                    """INSERT INTO users (username, email, salt, password_hash)
                       VALUES (?, ?, ?, ?)""",
                    (username, email, salt, digest),
                )
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Account already exists",
                "That username or email is already registered.",
            )
            return
        except sqlite3.Error as exc:
            messagebox.showerror("Database error", f"Could not create account:\n{exc}")
            return

        messagebox.showinfo("Account created", "Your account is ready. Please log in.")
        self.show_login()

    def login(self):
        identity = self.login_identity.get().strip()
        password = self.login_password.get()

        if not identity or not password:
            messagebox.showwarning(
                "Missing information", "Enter your username/email and password."
            )
            return

        try:
            with sqlite3.connect(DB_NAME) as conn:
                row = conn.execute(
                    """SELECT id, username, salt, password_hash
                       FROM users
                       WHERE username = ? COLLATE NOCASE
                          OR email = ? COLLATE NOCASE""",
                    (identity, identity),
                ).fetchone()
        except sqlite3.Error as exc:
            messagebox.showerror("Database error", f"Could not log in:\n{exc}")
            return

        if row is None:
            messagebox.showerror("Login failed", "Invalid username/email or password.")
            return

        user_id, username, salt, saved_hash = row
        _, candidate_hash = hash_password(password, salt)

        if not hmac.compare_digest(candidate_hash, saved_hash):
            messagebox.showerror("Login failed", "Invalid username/email or password.")
            return

        self.current_user = {"id": user_id, "username": username}
        self.show_dashboard()

    def show_dashboard(self):
        self._clear_screen()
        wrapper = tk.Frame(self.container, bg=BG, padx=36, pady=28)
        wrapper.pack(fill="both", expand=True)

        header = tk.Frame(wrapper, bg=BG)
        header.pack(fill="x")
        tk.Label(
            header, text="NOVA", bg=BG, fg=ACCENT,
            font=("Segoe UI", 15, "bold")
        ).pack(side="left")
        tk.Button(
            header, text="Log out", command=self.logout,
            bg=FIELD, fg=TEXT, activebackground="#263853",
            activeforeground=TEXT, relief="flat", bd=0,
            cursor="hand2", padx=18, pady=9,
            font=("Segoe UI", 10, "bold")
        ).pack(side="right")

        tk.Label(
            wrapper,
            text=f"Welcome, {self.current_user['username']}!",
            bg=BG, fg=TEXT, font=("Segoe UI", 27, "bold")
        ).pack(anchor="w", pady=(60, 8))
        tk.Label(
            wrapper,
            text="You're logged in. This is your personal dashboard.",
            bg=BG, fg=MUTED, font=("Segoe UI", 12)
        ).pack(anchor="w", pady=(0, 28))

        cards = tk.Frame(wrapper, bg=BG)
        cards.pack(fill="x")
        for title, detail in [
            ("YOUR PROFILE", self.current_user["username"]),
            ("ACCOUNT STATUS", "Active session"),
            ("APPLICATION", "Tkinter + SQLite"),
        ]:
            tile = tk.Frame(cards, bg=PANEL, padx=20, pady=22)
            tile.pack(side="left", fill="both", expand=True, padx=(0, 12))
            tk.Label(
                tile, text=title, bg=PANEL, fg=MUTED,
                font=("Segoe UI", 9, "bold")
            ).pack(anchor="w")
            tk.Label(
                tile, text=detail, bg=PANEL, fg=TEXT,
                font=("Segoe UI", 12, "bold")
            ).pack(anchor="w", pady=(12, 0))

        tk.Label(
            wrapper,
            text="Demo dashboard — add profile editing, settings, or reports next.",
            bg=BG, fg=MUTED, font=("Segoe UI", 10)
        ).pack(anchor="w", side="bottom", pady=(20, 0))

        self.bind("<Return>", lambda event: None)

    def logout(self):
        self.current_user = None
        self.show_login()


if __name__ == "__main__":
    app = AuthApp()
    app.mainloop()
