
from prac_08.car import Car
import random

class Car(UnreliableCar):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):


