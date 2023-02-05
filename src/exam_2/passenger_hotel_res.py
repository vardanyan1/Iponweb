from typing import Dict

class Passenger:
    def __init__(self, name: str, city: str, rooms: Dict[str, int]):
        self.__name = name
        self.__city = city
        self.__rooms = rooms

    def __repr__(self):
        return f"{self.__name} from {self.__city}, took rooms: {self.__rooms}"

    """
    NAME, CITY, ROOMS getter
    """

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, key, value):
        self.__rooms[key] = value

    def reserve(self, hotel: "Hotel", type: str, count: int):
        hotel.reserve_rooms(type, count)
        if type in self.rooms.keys():
            self.rooms[type] += count
        else:
            self.rooms[type] = count


class Hotel:
    def __init__(self, city: str, rooms: Dict[str, int]):
        self.__city = city
        self.rooms = rooms

    def __repr__(self):
        return f"Hotel in {self.__city}, with rooms: {self.rooms}"

    @property
    def city(self):
        return self.__city

    def free_rooms_list(self, type: str):
        return self.rooms[type]

    def reserve_rooms(self, type: str, count: int):
        if self.free_rooms_list(type) < count:
            print(f"There is no enough rooms, only have: {self.free_rooms_list(type)}")

        else:
            self.rooms[type] -= count
            print(f"Reserved {count} {type} in {self.__city} hotel")

def book():
    hotel1 = Hotel("Yerevan", {"penthouse": 2, "single": 40, "double": 30})
    pas1 = Passenger("Adam", "Gyumri", {})
    print(f"Created: {hotel1}")
    hotel1.reserve_rooms("single", 4)
    print(f"After reservation: {hotel1}")
    pas1.reserve(hotel1, "double", 2)
    print(f"{pas1}")
    print(f"After reservation: {hotel1}")


book()
