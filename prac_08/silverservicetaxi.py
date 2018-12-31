
from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness=0.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.flagfall = 4.5
        self.current_fare_distance = 0

    def __str__(self):
        return "{}, {}, ${}/km plus flagfall of, ${}".format(super().__str__(), self.current_fare_distance,
                                                             self.fanciness, self.flagfall)

    def get_fare(self):
        return self.price_per_km * self.fanciness

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

