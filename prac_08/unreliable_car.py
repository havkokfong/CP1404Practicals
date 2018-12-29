
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.driven_distance = 0

    def __str__(self):
        return "{}, {} car reliability, {} driven distance".format(super().__str__(), self.reliability,
                                                                   self.driven_distance)

    def drive(self, distance):
        if distance < self.reliability:
            drive_distance = super().drive(distance)
            self.driven_distance += drive_distance
            return drive_distance



