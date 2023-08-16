import tkinter as tk
from tkinter import ttk

class ReservationTableView(ttk.Treeview):
    def __init__(self, master):
        super().__init__(master)
        
        self["columns"] = ("Check-In", "Check-Out")
        self.heading("#1", text="Check-In")
        self.heading("#2", text="Check-Out")
        self.column("#1", anchor="center")
        self.column("#2", anchor="center")

    def add_reservation(self, reservation):
        self.insert("", "end", values=(reservation.getCheckinDate(), reservation.getCheckoutDate()))

    def clear_table(self):
        self.delete(*self.get_children())
