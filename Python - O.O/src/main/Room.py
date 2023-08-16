class Room:
    def __init__(self, number="", name="", floor=1, description="", dimension=0.0, room_type=None):
        self.number = number
        self.name = name
        self.floor = floor
        self.description = description
        self.dimension = dimension
        self.room_type = room_type
        self.daily_rate = 0.0

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_floor(self):
        return self.floor

    def set_floor(self, floor):
        self.floor = floor

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_dimension(self):
        return self.dimension

    def set_dimension(self, dimension):
        self.dimension = dimension

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_daily_rate(self):
        return self.daily_rate

    def set_daily_rate(self, daily_rate):
        self.daily_rate = daily_rate

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Room):
            return False
        return self.floor == other.floor and self.number == other.number and self.name == other.name and self.room_type == other.room_type

    def __hash__(self):
        return hash((self.number, self.name, self.floor, self.room_type))

    def __str__(self):
        return f"Room{{number='{self.number}', name='{self.name}', floor={self.floor}, description='{self.description}', dimension={self.dimension}, room_type={self.room_type}}}"
