import tkinter as tk
import mysql.connector
import sql
import tkinter.messagebox
import customtkinter as ctk

class RegisterFrame(tk.Frame):
    def __init__(self, master, login_frame):
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame

        title = tk.Label(master=self, text="Registration", font=("Arial Bold", 28))
        title.grid(row=0, columnspan=2, padx=10, pady=(50, 20))

        subtitle = tk.Label(master=self, text="Please provide the following details:", font=("Arial", 13))
        subtitle.grid(row=1, columnspan=2, padx=10, pady=(0, 30))

        first_name_label = tk.Label(self, text="First Name:", font=("Arial", 13))
        first_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        # Entry widget for username
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        # Label for password
        last_name_label = tk.Label(self, text="Last Name:", font=("Arial", 13))
        last_name_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        # Entry widget for password (show="*" to hide the password)
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        email_label = tk.Label(self, text="Email:", font=("Arial", 13))
        email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Entry widget for username
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5, sticky="we")

        # Label for password
        password_label = tk.Label(self, text="Password:", font=("Arial", 13))
        password_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        # Entry widget for password (show="*" to hide the password)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=5, column=1, padx=5, pady=5, sticky="we")

        # Login button
        login_button = tk.Button(self, text="Register", font=("Arial", 13), command=lambda: self.register(self.login_frame))
        login_button.grid(row=8, column=0, columnspan=2, pady=(20, 10))

    def register(self, login_frame):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if first_name == "" or last_name == "" or password == "" or email == "":
            tk.messagebox.showinfo("Error", "Please fill out all details")
            return None

        if "@" not in email or ".com" not in email:
            self.email_entry.delete(0, tk.END)
            tk.messagebox.showinfo("Error", "Invalid Email. Please try again.")
            return None




        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        result = sql.register(first_name, last_name, email, password)

        if result == True:
            tk.messagebox.showinfo("Success", "Successfully registered. Returning to main menu")

        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
