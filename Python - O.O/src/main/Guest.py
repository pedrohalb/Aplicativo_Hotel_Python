from datetime import date

class Guest:
    def __init__(self, title, firstName, lastName, email, birthDate):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.birthDate = birthDate
        self.reservations = []

    def getName(self):
        return f"{self.firstName} {self.lastName}"

    def setFirstName(self, name):
        if len(name) > 2:
            self.firstName = name

    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        return self.lastName

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setBirthDate(self, birthDate):
        self.birthDate = birthDate

    def getBirthDate(self):
        return self.birthDate

    def getReservations(self):
        return self.reservations

    def setReservations(self, reservations):
        self.reservations = reservations

    def addReservation(self, reservation):
        self.reservations.append(reservation)

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def __str__(self):
        return f"Guest{{title={self.title}, firstName={self.firstName}, lastName={self.lastName}, email={self.email}, birthDate={self.birthDate}, reservations={self.reservations}}}"
