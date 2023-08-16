class RoomNotFoundException(Exception):
    def __init__(self, message, number):
        super().__init__(message)
        self.number = number
