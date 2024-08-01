from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """calculate the fare"""
        total_fare = super().get_fare() + self.flagfall
        return round(total_fare, 2)

    def __str__(self):
        """return the string"""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"
