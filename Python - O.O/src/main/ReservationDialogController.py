import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date

class ReservationDialogController:
    def __init__(self, parent):
        self.parent = parent
        self.reservation = None

        self.create_widgets()

    def create_widgets(self):
        # Labels e campos para selecionar as datas de check-in e check-out
        lbl_checkin = ttk.Label(self.parent, text="Data de Check-in:")
        lbl_checkin.grid(row=0, column=0, padx=5, pady=5)
        self.checkin_date_var = tk.StringVar()
        self.checkin_date_picker = ttk.Entry(self.parent, textvariable=self.checkin_date_var)
        self.checkin_date_picker.grid(row=0, column=1, padx=5, pady=5)

        lbl_checkout = ttk.Label(self.parent, text="Data de Check-out:")
        lbl_checkout.grid(row=1, column=0, padx=5, pady=5)
        self.checkout_date_var = tk.StringVar()
        self.checkout_date_picker = ttk.Entry(self.parent, textvariable=self.checkout_date_var)
        self.checkout_date_picker.grid(row=1, column=1, padx=5, pady=5)

        # Botões de Confirmação e Cancelamento
        btn_confirm = ttk.Button(self.parent, text="Confirmar", command=self.handle_confirm_button)
        btn_confirm.grid(row=2, column=0, padx=5, pady=10)

        btn_cancel = ttk.Button(self.parent, text="Cancelar", command=self.handle_cancel_button)
        btn_cancel.grid(row=2, column=1, padx=5, pady=10)

    def handle_confirm_button(self):
        checkin_date_str = self.checkin_date_var.get()
        checkout_date_str = self.checkout_date_var.get()

        if checkin_date_str and checkout_date_str:
            checkin_date = self.parse_date(checkin_date_str)
            checkout_date = self.parse_date(checkout_date_str)

            if checkin_date and checkout_date:
                self.reservation = (checkin_date, checkout_date)
                self.close_dialog()
            else:
                self.show_error_message("Datas inválidas. Por favor, use o formato 'dd/mm/aaaa'.")
        else:
            self.show_error_message("Por favor, preencha ambas as datas de check-in e check-out.")

    def handle_cancel_button(self):
        self.reservation = None
        self.close_dialog()

    def parse_date(self, date_str):
        try:
            day, month, year = map(int, date_str.split('/'))
            return date(year, month, day)
        except ValueError:
            return None

    def show_error_message(self, message):
        messagebox.showerror("Erro", message)

    def get_reservation(self):
        return self.reservation

    def close_dialog(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reserva - Sistema de Reservas de Hostel")

    reservation_dialog_controller = ReservationDialogController(root)

    root.mainloop()
