from datetime import date

class Reservation:
    def __init__(self, checkinDate=None, checkoutDate=None):
        self.reservationDate = date.today()
        self.checkinDate = checkinDate
        self.checkoutDate = checkoutDate

    def getReservationDate(self):
        return self.reservationDate

    def setReservationDate(self, reservationDate):
        self.reservationDate = reservationDate

    def getCheckinDate(self):
        return self.checkinDate

    def setCheckinDate(self, checkinDate):
        self.checkinDate = checkinDate

    def getCheckoutDate(self):
        return self.checkoutDate

    def setCheckoutDate(self, checkoutDate):
        self.checkoutDate = checkoutDate

    def __str__(self):
        return f"Reservation{{reservationDate={self.reservationDate}, checkinDate={self.checkinDate}, checkoutDate={self.checkoutDate}}}"
