import sqlite3
from enum import Enum

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

class RoomDAO:
    def __init__(self):
        self.conn = sqlite3.connect("meu_banco_de_dados.db")
        self.create_table()

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Rooms (
                                number TEXT PRIMARY KEY,
                                name TEXT NOT NULL,
                                floor INTEGER NOT NULL,
                                description TEXT,
                                dimension REAL,
                                roomType TEXT NOT NULL)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error creating table:", e)

    def salvar_room(self, room):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO Rooms (number, name, floor, description, dimension, roomType)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (room.number, room.name, room.floor, room.description, room.dimension, room.room_type.name))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error saving room:", e)

    def carregar_rooms(self):
        rooms = []
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Rooms")
            rows = cursor.fetchall()
            for row in rows:
                number = row[0]
                name = row[1]
                floor = row[2]
                description = row[3]
                dimension = row[4]
                room_type_str = row[5]
                room_type = RoomType[room_type_str]
                room = Room(number, name, floor, description, dimension, room_type)
                rooms.append(room)
        except sqlite3.Error as e:
            print("Error loading rooms:", e)
        return rooms

    def save_all_rooms(self, rooms):
        try:
            cursor = self.conn.cursor()
            cursor.executemany('''INSERT INTO Rooms (number, name, floor, description, dimension, roomType)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                               [(room.number, room.name, room.floor, room.description, room.dimension, room.room_type.name)
                                for room in rooms])
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error saving all rooms:", e)
