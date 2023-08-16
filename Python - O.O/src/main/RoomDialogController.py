from enum import Enum
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

class RoomDialogController:
    def __init__(self, parent):
        self.parent = parent
        self.room = None

        self.create_widgets()

    def create_widgets(self):
        # Labels e campos para número, nome, andar, descrição e dimensão do quarto
        lbl_number = ttk.Label(self.parent, text="Número:")
        lbl_number.grid(row=0, column=0, padx=5, pady=5)
        self.number_var = tk.StringVar()
        self.number_entry = ttk.Entry(self.parent, textvariable=self.number_var)
        self.number_entry.grid(row=0, column=1, padx=5, pady=5)

        lbl_name = ttk.Label(self.parent, text="Nome:")
        lbl_name.grid(row=1, column=0, padx=5, pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(self.parent, textvariable=self.name_var)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        lbl_floor = ttk.Label(self.parent, text="Andar:")
        lbl_floor.grid(row=2, column=0, padx=5, pady=5)
        self.floor_var = tk.IntVar()
        self.floor_entry = ttk.Entry(self.parent, textvariable=self.floor_var)
        self.floor_entry.grid(row=2, column=1, padx=5, pady=5)

        lbl_description = ttk.Label(self.parent, text="Descrição:")
        lbl_description.grid(row=3, column=0, padx=5, pady=5)
        self.description_var = tk.StringVar()
        self.description_entry = ttk.Entry(self.parent, textvariable=self.description_var)
        self.description_entry.grid(row=3, column=1, padx=5, pady=5)

        lbl_dimension = ttk.Label(self.parent, text="Dimensão:")
        lbl_dimension.grid(row=4, column=0, padx=5, pady=5)
        self.dimension_var = tk.DoubleVar()
        self.dimension_entry = ttk.Entry(self.parent, textvariable=self.dimension_var)
        self.dimension_entry.grid(row=4, column=1, padx=5, pady=5)

        # ComboBox para selecionar o tipo do quarto
        lbl_room_type = ttk.Label(self.parent, text="Tipo de Quarto:")
        lbl_room_type.grid(row=5, column=0, padx=5, pady=5)
        self.room_type_var = tk.StringVar()
        self.room_type_combobox = ttk.Combobox(self.parent, textvariable=self.room_type_var, values=[room_type.value for room_type in RoomType])
        self.room_type_combobox.grid(row=5, column=1, padx=5, pady=5)

        # Botões de Confirmação e Cancelamento
        btn_confirm = ttk.Button(self.parent, text="Confirmar", command=self.handle_confirm_button)
        btn_confirm.grid(row=6, column=0, padx=5, pady=10)

        btn_cancel = ttk.Button(self.parent, text="Cancelar", command=self.handle_cancel_button)
        btn_cancel.grid(row=6, column=1, padx=5, pady=10)

    def handle_confirm_button(self):
        number = self.number_var.get()
        name = self.name_var.get()
        floor = self.floor_var.get()
        description = self.description_var.get()
        dimension = self.dimension_var.get()
        room_type_str = self.room_type_var.get()

        if not (number and name and floor and description and dimension and room_type_str):
            self.show_error_message("Erro de entrada", "Todos os campos são obrigatórios.", "Preencha todos os campos antes de confirmar.")
            return

        try:
            dimension = float(dimension)
        except ValueError:
            self.show_error_message("Erro de entrada", "Valores inválidos", "A dimensão deve ser um número válido.")
            return

        room_type = None
        for rt in RoomType:
            if rt.value == room_type_str:
                room_type = rt
                break

        if room_type is None:
            self.show_error_message("Erro de entrada", "Tipo de quarto inválido", "Selecione um tipo de quarto válido.")
            return

        self.room = Room(number, name, floor, description, dimension, room_type)
        self.close_dialog()

    def handle_cancel_button(self):
        self.room = None
        self.close_dialog()

    def show_error_message(self, title, header, content):
        messagebox.showerror(title, f"{header}\n\n{content}")

    def get_room(self):
        return self.room

    def close_dialog(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Adicionar Quarto - Sistema de Reservas de Hostel")

    room_dialog_controller = RoomDialogController(root)

    root.mainloop()
