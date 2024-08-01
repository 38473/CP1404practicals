from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """returns the distance driven"""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
