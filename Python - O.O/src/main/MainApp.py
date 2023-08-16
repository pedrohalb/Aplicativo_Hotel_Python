from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from enum import Enum


class Title(Enum):
    MR = "MR"
    MRS = "MRS"
    MISS = "MISS"
    MS = "MS"
    DR = "DR"


class RoomType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    EXECUTIVE_SUITE = "Executive Suite"


class Room:
    def __init__(self, number, name, floor, description="", dimension=0.0, room_type=None):
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
        btn_make_reservation = ttk.Button(
            self.root, text="Fazer Reserva", command=self.handle_make_reservation_button
        )
        btn_make_reservation.grid(row=0, column=1, padx=10, pady=10)

    def handle_make_reservation_button(self):
        # Abrir a janela de fazer reserva
        make_reservation_window = MakeReservationWindow(self.root)

    def handle_list_guests_button(self):
        # Abrir a janela de listar hóspedes
        list_guests_window = ListGuestsWindow(self.root)


class MakeReservationWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Fazer Reserva")

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

        # Botão para confirmar a reserva
        tk.Button(self, text="Confirmar Reserva", command=self.handle_confirm_reservation).grid(
            row=3, column=0, columnspan=2, padx=10, pady=10
        )

    def handle_confirm_reservation(self):
        # Obter as datas de check-in e check-out dos widgets
        checkin_date_str = self.checkin_var.get()
        checkout_date_str = self.checkout_var.get()

        # Converter as datas para o formato datetime
        try:
            checkin_date = datetime.strptime(checkin_date_str, "%d/%m/%Y").date()
            checkout_date = datetime.strptime(checkout_date_str, "%d/%m/%Y").date()

            # Verificar se a data de check-out é posterior à data de check-in
            if checkout_date <= checkin_date:
                messagebox.showerror("Erro", "A data de Check-out deve ser posterior à data de Check-in.")
                return

            # Adicionar a reserva à lista de reservas
            new_reservation = Reservation(checkin_date, checkout_date)

            # Chamar o método para adicionar a reserva à lista do MakeReservationController
            MakeReservationController.add_reservation(new_reservation)

            # Fechar a janela de fazer reserva
            self.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd/mm/yyyy.")


class MakeReservationController:
    reservation_list = []

    @classmethod
    def add_reservation(cls, reservation):
        cls.reservation_list.append(reservation)


class ListGuestsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Lista de Hóspedes")

        self.create_widgets()

    def create_widgets(self):
        # Adicione aqui os widgets para listar os hóspedes
        columns = ("Nome", "Telefone", "Email")
        self.guest_table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.guest_table.heading(col, text=col)
        self.guest_table.grid(row=0, column=0, padx=5, pady=5)

        # Botão para adicionar um hóspede
        tk.Button(self, text="Adicionar Hóspede", command=self.handle_add_guest).grid(
            row=1, column=0, padx=5, pady=10
        )

        # Fechar a janela ao clicar no botão "Fechar"
        tk.Button(self, text="Fechar", command=self.destroy).grid(row=2, column=0, padx=5, pady=10)

        # Adicionar aqui os hóspedes à tabela
        self.update_guest_table()

    def handle_add_guest(self):
        # Abrir a janela de adicionar hóspede
        guest_dialog = GuestDialog(self)

        # Aguardar o fechamento da janela de diálogo antes de atualizar a tabela
        self.wait_window(guest_dialog)

        # Atualizar a tabela de hóspedes na janela ListGuestsWindow
        self.update_guest_table()
        
    def update_guest_table(self):
        # Limpar a tabela
        self.guest_table.delete(*self.guest_table.get_children())

        # Preencher a tabela com os hóspedes na lista
        for guest in GuestDialogController.guest_list:
            self.guest_table.insert("", "end", values=(guest.name, guest.phone, guest.email))


class Guest:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class GuestDialogController:
    guest_list = []

    @classmethod
    def add_guest(cls, guest):
        cls.guest_list.append(guest)


class GuestDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Adicionar Hóspede")

        # Variáveis para armazenar os dados do hóspede
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Widgets para coletar os dados do hóspede
        tk.Label(self, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.name_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Telefone:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.phone_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.email_var).grid(row=2, column=1, padx=5, pady=5)

        # Botão para confirmar o hóspede
        tk.Button(self, text="Confirmar Hóspede", command=self.handle_confirm_guest).grid(
            row=3, column=0, columnspan=2, padx=10, pady=10
        )

    def handle_confirm_guest(self):
        # Obter os dados do hóspede dos widgets
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()

        # Criar um novo objeto Guest
        new_guest = Guest(name, phone, email)

        # Adicionar o hóspede à lista de hóspedes
        GuestDialogController.add_guest(new_guest)

        # Atualizar a tabela de hóspedes na janela ListGuestsWindow
        list_guests_window = self.master
        list_guests_window.update_guest_table()

        # Fechar a janela de diálogo de adicionar hóspede
        self.destroy()
        
class RoomDialogController:
    room_list = []

    @classmethod
    def add_room(cls, room):
        cls.room_list.append(room)


class RoomDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Adicionar Quarto")

        # Variáveis para armazenar as informações do novo quarto
        self.number_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.floor_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.dimension_var = tk.DoubleVar()
        self.room_type_var = tk.StringVar()
        self.room_type_var.set(RoomType.SINGLE.value)  # Valor padrão para o tipo do quarto

        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Adicionar Quarto", command=self.handle_add_room).grid(
            row=7, column=0, columnspan=2, padx=10, pady=10)
        # Widgets para coletar informações do quarto
        tk.Label(self, text="Número do Quarto:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.number_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Nome do Quarto:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.name_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Andar:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.floor_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="Descrição:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.description_var).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text="Dimensão:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.dimension_var).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self, text="Tipo de Quarto:").grid(row=5, column=0, padx=5, pady=5)
        room_type_combobox = ttk.Combobox(self, textvariable=self.room_type_var, values=[t.value for t in RoomType])
        room_type_combobox.grid(row=5, column=1, padx=5, pady=5)
        
        # Botão para confirmar o novo quarto
        tk.Button(self, text="Confirmar", command=self.handle_confirm_room).grid(
            row=6, column=0, columnspan=2, padx=10, pady=10)
            
        tk.Button(self, text="Adicionar Quarto", command=self.handle_add_room).grid(
            row=7, column=0, columnspan=2, padx=10, pady=10)


    def handle_confirm_room(self):
        # Obter as informações do novo quarto dos widgets
        number = self.number_var.get()
        name = self.name_var.get()
        floor = self.floor_var.get()
        description = self.description_var.get()
        dimension = self.dimension_var.get()
        room_type_str = self.room_type_var.get()

        # Verificar se todos os campos foram preenchidos
        if not number or not name or not floor:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return

        # Converter o tipo do quarto para o enum RoomType
        room_type = RoomType(room_type_str)

        # Criar o objeto do quarto com as informações
        new_room = Room(number, name, floor, description, dimension, room_type)

        # Chamar o método para adicionar o quarto à lista do RoomDialogController
        RoomDialogController.add_room(new_room)

        # Fechar a janela de diálogo
        self.destroy()


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservas de Hostel")

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Labels
        lbl_username = ttk.Label(main_frame, text="Usuário:")
        lbl_username.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        lbl_password = ttk.Label(main_frame, text="Senha:")
        lbl_password.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        # Campos de entrada
        self.username_var = tk.StringVar()
        entry_username = ttk.Entry(main_frame, textvariable=self.username_var)
        entry_username.grid(row=0, column=1, padx=5, pady=5)

        self.password_var = tk.StringVar()
        entry_password = ttk.Entry(main_frame, textvariable=self.password_var, show="*")
        entry_password.grid(row=1, column=1, padx=5, pady=5)

        # Botões
        btn_login = ttk.Button(main_frame, text="Login", command=self.handle_login)
        btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def handle_login(self):
        # Adicione a lógica de autenticação aqui usando self.username_var.get() e self.password_var.get()
        # Por exemplo, você pode comparar os valores com credenciais fixas como no exemplo original em JavaFX

        # Exemplo básico apenas para ilustração
        username = self.username_var.get()
        password = self.password_var.get()

        if username == "pedro" and password == "henrique":
            self.show_success_message("Login bem-sucedido!")
            self.open_menu_screen()  # Chamando a próxima janela após o login bem-sucedido
        else:
            self.show_error_message("Credenciais inválidas! Por favor, tente novamente.")

    def show_success_message(self, message):
        messagebox.showinfo("Sucesso", message)

    def show_error_message(self, message):
        messagebox.showerror("Erro", message)

    def open_menu_screen(self):
        # Criar a próxima janela do menu principal aqui
        menu_controller = MenuController()
        self.root.withdraw()  # Esconde a janela de login
        menu_controller.root.deiconify()  # Exibe a janela do menu principal


if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApp(root)
    root.mainloop()
