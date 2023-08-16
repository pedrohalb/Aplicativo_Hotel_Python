import sqlite3
from datetime import date
from typing import List

from main.java.com.example.demo.MakeReservationController import Reservation

class ReservationDAO:
    @staticmethod
    def salvarReservation(reservation):
        try:
            with sqlite3.connect("meu_banco_de_dados.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Reservations (checkinDate, checkoutDate) VALUES (?, ?)",
                               (reservation.getCheckinDate().toString(), reservation.getCheckoutDate().toString()))
                conn.commit()
        except sqlite3.Error as e:
            print("Erro ao salvar reserva:", e)

    @staticmethod
    def carregarReservations() -> List[Reservation]:
        reservations = []
        try:
            with sqlite3.connect("meu_banco_de_dados.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Reservations")
                for row in cursor.fetchall():
                    checkinDate = date.fromisoformat(row[0])
                    checkoutDate = date.fromisoformat(row[1])
                    reservation = Reservation(checkinDate, checkoutDate)
                    reservations.append(reservation)
        except sqlite3.Error as e:
            print("Erro ao carregar reservas:", e)
        return reservations

    @staticmethod
    def saveAllReservations(reservations: List[Reservation]):
        try:
            with sqlite3.connect("meu_banco_de_dados.db") as conn:
                cursor = conn.cursor()
                conn.execute("BEGIN TRANSACTION")
                for reservation in reservations:
                    cursor.execute("INSERT INTO Reservations (checkinDate, checkoutDate) VALUES (?, ?)",
                                   (reservation.getCheckinDate().toString(), reservation.getCheckoutDate().toString()))
                conn.commit()
        except sqlite3.Error as e:
            print("Erro ao salvar todas as reservas:", e)
