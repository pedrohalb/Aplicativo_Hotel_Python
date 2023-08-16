import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from enum import Enum
from datetime import date

class Title(Enum):
    MR = "Mr."
    MRS = "Mrs."
    MS = "Ms."

class Guest:
    def __init__(self, title, first_name, last_name, email, birth_date):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date

class ListGuestsController:
    def __init__(self, menu_stage):
        self.menu_stage = menu_stage
        self.root = tk.Tk()
        self.root.title("Listar Hóspedes - Sistema de Reservas de Hostel")

        self.guests_list = []

        self.create_widgets()

    def create_widgets(self):
        # Tabela de hóspedes
        columns = ("Título", "Nome", "Sobrenome", "E-mail", "Data de Nascimento")
        self.guest_table = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.guest_table.heading(col, text=col)
        self.guest_table.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        # Botão de Voltar para o Menu Principal
        btn_back = ttk.Button(self.root, text="Voltar para o Menu Principal", command=self.back_to_menu)
        btn_back.grid(row=1, column=0, padx=5, pady=10)

    def back_to_menu(self):
        self.root.destroy()  # Fechar a janela de listagem de hóspedes
        self.menu_stage.deiconify()  # Mostrar o menu principal novamente

    def add_guest(self, title, first_name, last_name, email, birth_date):
        new_guest = Guest(title, first_name, last_name, email, birth_date)
        self.guests_list.append(new_guest)
        self.update_table()

    def update_table(self):
        self.guest_table.delete(*self.guest_table.get_children())
        for guest in self.guests_list:
            self.guest_table.insert("", "end", values=(guest.title.value, guest.first_name, guest.last_name, guest.email, guest.birth_date))

if __name__ == "__main__":
    menu_root = tk.Tk()
    menu_root.title("Menu Principal - Sistema de Reservas de Hostel")

    list_guests_controller = ListGuestsController(menu_root)

    menu_root.mainloop()
