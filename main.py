import tkinter as tk

from login import LoginFrame

class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title, width=1280, height=720):
        """
        Constructor for the Interface class,
        the main window for the HCMS.
        :param title: str
        :param width: int - default 960 pixels
        :param height: int - default 540 pixels
        """
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")


if __name__ == "__main__":
    # DO NOT MODIFY THIS
    expense_tracker = Interface("Mayank's Expense Tracker")
    login = LoginFrame(expense_tracker)
    login.pack(fill=tk.BOTH, expand=True)
    # login.place(relx=0.295, rely=0.05, relwidth=1, relheight=1)
    expense_tracker.mainloop()