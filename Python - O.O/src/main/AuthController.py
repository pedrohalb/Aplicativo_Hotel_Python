import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from enum import Enum
from datetime import date

class AuthController:
    FIXED_USERNAME = "pedro"
    FIXED_PASSWORD = "henrique"

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - Sistema de Reservas de Hostel")

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Label e Entry para o nome de usuário
        username_label = ttk.Label(self.root, text="Usuário:")
        username_label.grid(row=0, column=0, padx=5, pady=5)
        username_entry = ttk.Entry(self.root, textvariable=self.username_var)
        username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label e Entry para a senha
        password_label = ttk.Label(self.root, text="Senha:")
        password_label.grid(row=1, column=0, padx=5, pady=5)
        password_entry = ttk.Entry(self.root, textvariable=self.password_var, show="*")
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botão de login
        login_button = ttk.Button(self.root, text="Login", command=self.handle_login_button)
        login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def handle_login_button(self):
        username = self.username_var.get()
        password = self.password_var.get()
        is_authenticated = self.authenticate(username, password)

        if is_authenticated:
            self.show_success_alert("Login bem-sucedido!")
            self.open_menu_screen()
        else:
            self.show_error_alert("Credenciais inválidas! Por favor, tente novamente.")

    def authenticate(self, username, password):
        return username == self.FIXED_USERNAME and password == self.FIXED_PASSWORD

    def show_success_alert(self, message):
        messagebox.showinfo("Sucesso", message)

    def show_error_alert(self, message):
        messagebox.showerror("Erro", message)

    def open_menu_screen(self):
        self.root.destroy()  # Fechar a janela de login
        menu_controller = MenuController()
        menu_controller.root.mainloop()

        
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
        make_reservation_window = MakeReservationWindow(self.root)

    def handle_list_guests_button(self):
        # Abrir a janela de listar hóspedes
        list_guests_window = ListGuestsWindow(self.root)

# Implementação da janela de fazer reserva
class MakeReservationWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Fazer Reserva - Sistema de Reservas de Hostel")

        # Labels e Entrys para informações da reserva
        lbl_checkin = ttk.Label(self, text="Data de Check-in:")
        lbl_checkin.grid(row=0, column=0, padx=5, pady=5)
        entry_checkin = ttk.Entry(self)
        entry_checkin.grid(row=0, column=1, padx=5, pady=5)

        lbl_checkout = ttk.Label(self, text="Data de Check-out:")
        lbl_checkout.grid(row=1, column=0, padx=5, pady=5)
        entry_checkout = ttk.Entry(self)
        entry_checkout.grid(row=1, column=1, padx=5, pady=5)

        # Botões para confirmar ou cancelar a reserva
        btn_confirm = ttk.Button(self, text="Confirmar", command=self.handle_confirm_reservation)
        btn_confirm.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        btn_cancel = ttk.Button(self, text="Cancelar", command=self.destroy)
        btn_cancel.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Implementação da janela de listar hóspedes
class ListGuestsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Lista de Hóspedes - Sistema de Reservas de Hostel")

        self.guest_list = []  # Lista para armazenar os dados dos hóspedes

        self.create_widgets()

    def create_widgets(self):
        # Treeview para exibir a lista de hóspedes
        guest_tree = ttk.Treeview(self, columns=("First Name", "Last Name", "Email", "Birth Date"), show="headings")
        guest_tree.heading("First Name", text="Nome")
        guest_tree.heading("Last Name", text="Sobrenome")
        guest_tree.heading("Email", text="Email")
        guest_tree.heading("Birth Date", text="Data de Nascimento")
        guest_tree.grid(row=0, column=0, padx=10, pady=10)

        # Botão para atualizar a lista de hóspedes
        btn_refresh = ttk.Button(self, text="Atualizar", command=self.update_guest_list)
        btn_refresh.grid(row=1, column=0, padx=10, pady=5)

        # Botão para fechar a janela
        btn_close = ttk.Button(self, text="Fechar", command=self.destroy)
        btn_close.grid(row=2, column=0, padx=10, pady=5)

        self.update_guest_list()  # Atualiza a lista de hóspedes na inicialização

    def update_guest_list(self):
        # Atualiza a lista de hóspedes exibida no Treeview
        guest_tree = self.children['!treeview']
        guest_tree.delete(*guest_tree.get_children())  # Limpa a exibição atual

        for guest in self.guest_list:
            guest_tree.insert("", "end", values=(guest.first_name, guest.last_name, guest.email, guest.birth_date))


if __name__ == "__main__":
    app = AuthController()
    app.root.mainloop()