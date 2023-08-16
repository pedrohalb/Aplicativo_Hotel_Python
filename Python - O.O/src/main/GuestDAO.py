import sqlite3
from datetime import datetime
from main.java.com.example.demo.Guest import Guest

from main.java.com.example.demo.ListGuestsController import Title

class GuestDAO:
    @staticmethod
    def salvar_guest(guest):
        try:
            conn = sqlite3.connect("meu_banco_de_dados.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Guests (title, firstName, lastName, email, birthDate) VALUES (?, ?, ?, ?, ?)",
                           (guest.title.name, guest.first_name, guest.last_name, guest.email, guest.birth_date))

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Erro ao salvar o guest:", e)

    @staticmethod
    def carregar_guests():
        guests = []
        try:
            conn = sqlite3.connect("meu_banco_de_dados.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Guests")
            rows = cursor.fetchall()

            for row in rows:
                title_str, first_name, last_name, email, birth_date_str = row
                title = Title[title_str]
                birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
                guest = Guest(title, first_name, last_name, email, birth_date)
                guests.append(guest)

            conn.close()
        except sqlite3.Error as e:
            print("Erro ao carregar guests:", e)

        return guests
