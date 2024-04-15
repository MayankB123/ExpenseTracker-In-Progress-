import tkinter as tk
from tkinter import ttk
from sql import add_income

class AddIncomeFrame(tk.Toplevel):
    def __init__(self, master, dashboard_frame, user):
        super().__init__(master)
        self.master = master
        self.dashboard_frame = dashboard_frame
        self.user = user
        self.title("Income Entry")

        # Name Entry
        self.name_label = tk.Label(self, text="Name of income:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.date_label = tk.Label(self, text="Date of Income:")
        self.date_label.grid(row=1, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        self.category_label = tk.Label(self, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, pady=5)
        self.category_var = tk.StringVar(self)
        self.category_dropdown = ttk.Combobox(self, textvariable=self.category_var,
                                              values=["Wage", "Side Hustle", "Other"])
        self.category_dropdown.grid(row=2, column=1, padx=10, pady=5)

        # Amount Entry
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.grid(row=3, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=3, column=1, padx=10, pady=5)



        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def submit(self):
        amount = self.amount_entry.get()
        category = self.category_var.get()
        name = self.name_entry.get()
        date = self.date_entry.get()
        # Do something with the collected data (e.g., save to a database)
        add_income(self.user, name, date, category, amount)
        self.destroy()