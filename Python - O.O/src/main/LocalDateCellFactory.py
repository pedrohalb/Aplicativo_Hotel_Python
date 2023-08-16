import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class LocalDateCellFactory(ttk.Treeview):
    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent, columns=("date",), show="headings")
        self.heading("#1", text="Data")
        self.column("#1", anchor="center")
        self.column("#0", width=0, stretch=tk.NO)

        self.date_picker = DateEntry(self, date_pattern="dd/mm/yyyy", width=12, background="darkblue", foreground="white", borderwidth=2)
        self.date_picker.bind("<FocusOut>", self.on_date_picker_focus_out)
        self.date_picker.bind("<Return>", self.on_date_picker_return)

    def set_date(self, date_value):
        self.date_picker.set_date(date_value)

    def on_date_picker_focus_out(self, event):
        self.commit_edit()

    def on_date_picker_return(self, event):
        self.commit_edit()

    def edit_cell(self):
        self.date_picker.place(x=self.winfo_x(), y=self.winfo_y())
        self.date_picker.lift()

    def commit_edit(self):
        if self.date_picker.winfo_ismapped():
            new_value = self.date_picker.get_date()
            event = {
                "widget": self,
                "column": "#1",
                "row": self.identify_row(event.y),
                "value": new_value,
            }
            self.event_generate("<<TreeviewEditCommit>>", event=event)
            self.date_picker.place_forget()
