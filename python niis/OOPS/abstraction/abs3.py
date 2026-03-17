from abc import *

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")


v1 = Car("Honda")
v1.start()

v2 = Bike("Yamaha")
v2.start()