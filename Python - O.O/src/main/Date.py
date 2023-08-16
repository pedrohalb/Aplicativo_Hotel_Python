class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def convert_to_date(local_date):
        if local_date is not None:
            return Date(
                local_date.day,
                local_date.month,
                local_date.year
            )
        return None

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def get_month(self):
        return self.month

    def set_month(self, month):
        self.month = month

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
