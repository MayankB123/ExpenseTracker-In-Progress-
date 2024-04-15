import tkinter as tk
from tkinter import ttk
from AddIncome import AddIncomeFrame
from AddExpense import AddExpenseFrame
from matplotlib.figure import Figure
from sql import get_income
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta

class DashboardFrame(tk.Frame):
    def __init__(self, master, login_frame, user):
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.user = user

        num_rows = 2
        num_cols = 2

        income = get_income(user)
        total_income = 0
        for i in income:
            total_income += i[4]

        print(total_income)

        # Configure rows and columns in the frame
        for i in range(num_rows):
            self.rowconfigure(i, weight=1)  # Each row has equal weight for expansion
        for j in range(num_cols):
            self.columnconfigure(j, weight=1)

        # Create a Figure and a subplot
        fig = Figure(figsize=(4, 5), dpi=100)
        plot = fig.add_subplot(1, 1, 1)

        # Assuming today's date as the end date
        end_date = datetime.today()
        # Calculate the start date by subtracting 14 days
        start_date = end_date - timedelta(days=14)

        # Generate x values for each day in the last two weeks
        date_range = [start_date + timedelta(days=i) for i in range(14)]
        x = [date.strftime('%Y-%m-%d') for date in date_range]

        # Assuming y values (can be replaced with actual data retrieval)
        # Here, generating random y values for demonstration
        import random
        y = [random.randint(1, 20) for _ in range(14)]

        # Plotting data on the existing plot
        plot.plot(x, y, marker='o')

        # Rotate x-axis labels for better readability
        plot.set_xticklabels(x, rotation=45, ha='right')

        # Set labels and title
        plot.set_xlabel('Date')
        plot.set_ylabel('Value')
        plot.set_title('Data for the Last Two Weeks')

        # Display grid
        plot.grid(True)

        # Create a canvas to render the figure without displaying it
        canvas = FigureCanvasTkAgg(fig)
        canvas.draw()

        # Save the plot to a file or display it as desired
        # canvas.print_figure('plot.png', dpi=100)  # Example: save to a file
        # plt.show()  # Example: display the plot

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, sticky="nesw")

        add_income_button = tk.Button(self, text="Add Income", command=lambda: self.add_income())
        add_income_button.grid(row=1, column=0, sticky="ew")
        income_button = tk.Button(self, text="Add Expense", command=lambda: self.add_expense())
        income_button.grid(row=1, column=1, sticky="ew")


    def add_expense(self):
        add_expense = AddExpenseFrame(self.master, self, self.user)

    def add_income(self):
        add_income = AddIncomeFrame(self.master, self, self.user)





