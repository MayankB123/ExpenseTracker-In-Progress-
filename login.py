import tkinter as tk
from tkinter import ttk
from register import RegisterFrame
import sql
from dashboard import DashboardFrame



class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        num_rows = 11
        num_cols = 4

        # Configure rows and columns in the frame
        for i in range(num_rows):
            self.rowconfigure(i, weight=1)  # Each row has equal weight for expansion
        for j in range(num_cols):
            self.columnconfigure(j, weight=1)


        title = tk.Label(master=self, text="Mayank's Expense Tracker", font=("Arial Bold", 28))
        title.grid(row=0, column=1, columnspan=2, padx=10, pady=(50, 10))

        subtitle = tk.Label(master=self, text="Mayank's expense tracker is made to help you manage your expenses!", font=("Arial", 13))
        subtitle.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        login_text = tk.Label(master=self, text="Login", font=("Arial", 18))
        login_text.grid(row=3, column=1, columnspan=2, padx=10, pady=(50, 15))

        email_label = tk.Label(self, text="Email:", font=("Arial", 13))
        email_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")

        # Entry widget for username
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=2, padx=20, pady=5, sticky="we")

        # Label for password
        password_label = tk.Label(self, text="Password:", font=("Arial", 13))
        password_label.grid(row=5, column=1, padx=10, pady=5, sticky="e")

        # Entry widget for password (show="*" to hide the password)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=5, column=2, padx=20, pady=5, sticky="we")

        # Login button
        login_button = tk.Button(self, text="Login", font=("Arial", 13), command=lambda: self.login())
        login_button.grid(row=8, column=1, columnspan=2, pady=(20, 10))

        register_text = tk.Label(master=self, text="Don't have an account?", font=("Arial", 13))
        register_text.grid(row=9, column=1, columnspan=2, padx=10, pady=(40, 0))

        register_button = tk.Button(self, text="Register", font=("Arial", 13), command=self.register)
        register_button.grid(row=10, column=1, columnspan=2, pady=(20, 30))

        exit_button = tk.Button(master=self, text="Exit to Desktop", font=("Arial", 13), command=lambda: quit())
        exit_button.grid(row=11, column=1, columnspan=2, pady=50)


    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        user = sql.login(email, password)

        if user == False:
            return None


        self.pack_forget()
        dashboard = DashboardFrame(self.master, self, user)
        dashboard.pack(fill=tk.BOTH, expand = True)

    def register(self):
        self.pack_forget()

        # Create and display the Patient login frame
        register_frame = RegisterFrame(self.master, self)
        register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
