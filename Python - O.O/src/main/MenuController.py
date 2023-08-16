from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MakeReservationController import Reservation

class MenuController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Principal - Sistema de Reservas de Hostel")

        self.create_widgets()

    def create_widgets(self):
        # Botão para listar hóspedes
        btn_list_guests = ttk.Button(self.root, text="Lista de Hóspedes", command=self.handle_list_guests_button)
        btn_list_guests.grid(row=0, column=0, padx=10, pady=10)

        # Botão para fazer reserva
        btn_make_reservation = ttk.Button(self.root, text="Fazer Reserva", command=self.handle_make_reservation_button)
        btn_make_reservation.grid(row=0, column=1, padx=10, pady=10)

    def handle_make_reservation_button(self):
        # Abrir a janela de fazer reserva
        make_reservation_window = MakeReservationWindow(self.root, self.reservation_list, self.room_list)


    def handle_list_guests_button(self):
        # Abrir a janela de listar hóspedes
        list_guests_window = ListGuestsWindow(self.root)
    
class MakeReservationWindow(tk.Toplevel):
    def __init__(self, master, reservation_list, room_list):
        super().__init__(master)
        self.title("Fazer Reserva")

        self.reservation_list = reservation_list  # Lista de reservas
        self.room_list = room_list  # Lista de quartos

        # Variáveis para armazenar as datas de check-in e check-out
        self.checkin_var = tk.StringVar()
        self.checkout_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Widgets para coletar as datas de check-in e check-out
        tk.Label(self, text="Data de Check-in (dd/mm/yyyy):").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.checkin_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Data de Check-out (dd/mm/yyyy):").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.checkout_var).grid(row=1, column=1, padx=5, pady=5)

        # ComboBox para selecionar o quarto
        tk.Label(self, text="Selecione o Quarto:").grid(row=2, column=0, padx=5, pady=5)
        self.room_var = tk.StringVar()
        room_combobox = ttk.Combobox(self, textvariable=self.room_var, values=self.get_available_rooms())
        room_combobox.grid(row=2, column=1, padx=5, pady=5)

        # Botão para confirmar a reserva
        tk.Button(self, text="Confirmar Reserva", command=self.handle_confirm_reservation).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def get_available_rooms(self):
        # Retorna uma lista com os números dos quartos disponíveis para reserva
        return [room.number for room in self.room_list]

    def handle_confirm_reservation(self):
        # Obter as datas de check-in e check-out dos widgets
        checkin_date_str = self.checkin_var.get()
        checkout_date_str = self.checkout_var.get()

        # Converter as datas para o formato date
        try:
            checkin_date = date.strptime(checkin_date_str, "%d/%m/%Y")
            checkout_date = date.strptime(checkout_date_str, "%d/%m/%Y")

            # Verificar se a data de check-out é posterior à data de check-in
            if checkout_date <= checkin_date:
                messagebox.showerror("Erro", "A data de Check-out deve ser posterior à data de Check-in.")
                return

            # Obter o número do quarto selecionado
            room_number = self.room_var.get()

            # Verificar se o quarto está disponível
            room = self.get_room_by_number(room_number)
            if room is None:
                messagebox.showerror("Erro", f"O quarto {room_number} não está disponível para reserva.")
                return

            # Adicionar a reserva à lista de reservas
            new_reservation = Reservation(checkin_date, checkout_date)
            self.reservation_list.append(new_reservation)

            # Fechar a janela de fazer reserva
            self.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd/mm/yyyy.")

    def get_room_by_number(self, room_number):
        # Retorna o objeto do quarto pelo número, ou None se não encontrado
        for room in self.room_list:
            if room.number == room_number:
                return room
        return None
    
class ListGuestsWindow(tk.Toplevel):
    def __init__(self, master, guest_list):
        super().__init__(master)
        self.title("Lista de Hóspedes")

        self.guest_list = guest_list
        self.create_widgets()

    def create_widgets(self):
        # Adicione aqui os widgets para listar os hóspedes
        columns = ("Nome", "Telefone", "Email")
        self.guest_table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.guest_table.heading(col, text=col)
        self.guest_table.grid(row=0, column=0, padx=5, pady=5)

        # Adicione aqui os hóspedes à tabela
        for guest in self.guest_list:
            self.guest_table.insert("", "end", values=(guest.name, guest.phone, guest.email))

        # Fechar a janela ao clicar no botão "Fechar"
        tk.Button(self, text="Fechar", command=self.destroy).grid(row=1, column=0, padx=5, pady=10)


if __name__ == "__main__":
    menu_controller = MenuController()
    menu_controller.root.mainloop()
