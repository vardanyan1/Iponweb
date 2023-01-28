from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def __init__(self, wheels: int, doors: int, speed: int):
        pass

    @abstractmethod
    def get_max_speed_miles(self):
        pass

    @abstractmethod
    def get_max_speed_in_kilometers(self):
        pass

    @abstractmethod
    def how_many_doors(self):
        pass


class Car(Vehicle):
    def __init__(self, max_speed, doors):
        self.max_speed = max_speed
        self.doors = doors

    def get_max_speed_miles(self):
        return self.max_speed

    def get_max_speed_in_kilometers(self):
        return self.max_speed * 1.72

    def how_many_doors(self):
        return self.doors



