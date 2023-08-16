import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from enum import Enum
from datetime import date

class RoomType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    DELUXE = "Deluxe"

class Room:
    def __init__(self, number, name, floor, description, dimension, room_type):
        self.number = number
        self.name = name
        self.floor = floor
        self.description = description
        self.dimension = dimension
        self.room_type = room_type

class Reservation:
    def __init__(self, checkin_date, checkout_date):
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date

class LocalDateCellFactory(ttk.Treeview):
    def __init__(self, parent, date_format="%d/%m/%Y"):
        ttk.Treeview.__init__(self, parent, columns=("date",))
        self.date_format = date_format
        self.heading("#1", text="Data")
        self.column("#1", anchor="center")
        self.column("#0", width=0, stretch=tk.NO)

    def set_date(self, date_value):
        self.delete(*self.get_children())
        if date_value is not None:
            self.insert("", "end", values=(date_value.strftime(self.date_format),))

class MakeReservationController:
    def __init__(self, menu_stage):
        self.menu_stage = menu_stage
        self.root = tk.Tk()
        self.root.title("Fazer Reserva - Sistema de Reservas de Hostel")

        self.reservation_list = []
        self.room_list = []

        self.create_widgets()

    def create_widgets(self):
        # Tabela de reservas
        columns = ("Data de Check-in", "Data de Check-out")
        self.reservation_table = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.reservation_table.heading(col, text=col)
        self.reservation_table.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        # Botões para adicionar quarto e reserva
        btn_add_room = ttk.Button(self.root, text="Adicionar Quarto", command=self.handle_add_room_button)
        btn_add_room.grid(row=1, column=0, padx=5, pady=10)

        btn_add_reservation = ttk.Button(self.root, text="Adicionar Reserva", command=self.handle_add_reservation_button)
        btn_add_reservation.grid(row=1, column=1, padx=5, pady=10)

    def handle_add_room_button(self):
        # Abrir a janela para adicionar um quarto
        add_room_window = AddRoomWindow(self.root, self.room_list, self.update_table)


    def handle_add_reservation_button(self):
        # Abrir a janela para adicionar uma reserva
        add_reservation_window = AddReservationWindow(self.root, self.add_reservation, self.update_table)

    def back_to_menu(self):
        self.root.destroy()  # Fechar a janela de fazer reserva
        self.menu_stage.deiconify()  # Mostrar o menu principal novamente

    def add_reservation(self, checkin_date, checkout_date):
        new_reservation = Reservation(checkin_date, checkout_date)
        self.reservation_list.append(new_reservation)
        self.update_table()

    def update_table(self):
        self.reservation_table.delete(*self.reservation_table.get_children())
        for reservation in self.reservation_list:
            self.reservation_table.insert("", "end", values=(reservation.checkin_date, reservation.checkout_date))
            
class AddRoomWindow(tk.Toplevel):
    def __init__(self, master, room_list, update_table):
        super().__init__(master)
        self.title("Adicionar Quarto")

        self.room_list = room_list  # Lista de quartos para armazenar os novos quartos
        self.update_table = update_table  # Função para atualizar a tabela de reservas

        # Variáveis para armazenar os detalhes do quarto
        self.number_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.floor_var = tk.IntVar()
        self.description_var = tk.StringVar()
        self.dimension_var = tk.DoubleVar()
        self.room_type_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Widgets para coletar os detalhes do quarto
        tk.Label(self, text="Número:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.number_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Nome:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.name_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Andar:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.floor_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="Descrição:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.description_var).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text="Dimensão:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.dimension_var).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self, text="Tipo de Quarto:").grid(row=5, column=0, padx=5, pady=5)
        room_type_combo = ttk.Combobox(self, textvariable=self.room_type_var, values=[room_type.value for room_type in RoomType])
        room_type_combo.grid(row=5, column=1, padx=5, pady=5)

        # Botão para confirmar a adição do quarto
        tk.Button(self, text="Confirmar", command=self.handle_confirm_button).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def handle_confirm_button(self):
        # Obter os valores dos widgets
        number = self.number_var.get()
        name = self.name_var.get()
        floor = self.floor_var.get()
        description = self.description_var.get()
        dimension = self.dimension_var.get()
        room_type = self.room_type_var.get()

        # Verificar se todos os campos estão preenchidos
        if not all([number, name, floor, description, dimension, room_type]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        # Verificar se a dimensão é um número válido
        try:
            dimension = float(dimension)
        except ValueError:
            messagebox.showerror("Erro", "A dimensão deve ser um número válido.")
            return

        # Criar um novo objeto de quarto e adicioná-lo à lista
        new_room = Room(number, name, floor, description, dimension, room_type)
        self.room_list.append(new_room)

        # Fechar a janela de adicionar quarto
        self.destroy()

        # Atualizar a tabela de reservas na janela principal
        self.update_table()
        
class AddReservationWindow(tk.Toplevel):
    def __init__(self, master, add_reservation_callback, update_table_callback):
        super().__init__(master)
        self.title("Adicionar Reserva")

        self.add_reservation_callback = add_reservation_callback  # Função para adicionar reserva à lista
        self.update_table_callback = update_table_callback  # Função para atualizar a tabela de reservas

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

        # Botão para confirmar a adição da reserva
        tk.Button(self, text="Confirmar", command=self.handle_confirm_button).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def handle_confirm_button(self):
        # Obter as datas de check-in e check-out dos widgets
        checkin_date_str = self.checkin_var.get()
        checkout_date_str = self.checkout_var.get()

        # Converter as datas para o formato date
        try:
            checkin_date = date.strptime(checkin_date_str, "%d/%m/%Y")
            checkout_date = date.strptime(checkout_date_str, "%d/%m/%Y")

            # Verificar se a data de check-out é após a data de check-in
            if checkout_date <= checkin_date:
                messagebox.showerror("Erro", "A data de Check-out deve ser posterior à data de Check-in.")
                return

            # Adicionar a reserva à lista usando a função de callback
            self.add_reservation_callback(checkin_date, checkout_date)

            # Fechar a janela de adicionar reserva
            self.destroy()

            # Atualizar a tabela de reservas na janela principal usando a função de callback
            self.update_table_callback()

        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd/mm/yyyy.")

if __name__ == "__main__":
    menu_root = tk.Tk()
    menu_root.title("Menu Principal - Sistema de Reservas de Hostel")

    make_reservation_controller = MakeReservationController(menu_root)

    menu_root.mainloop()
