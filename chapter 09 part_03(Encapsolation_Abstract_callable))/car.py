"""A class that can be used to represent a car."""

class Car():
    """A single attempt to represent a car """
    def __init__(self, make : str , model: str , year : int) -> None:
        self.make : str = make
        self.model : str = model
        self.year : int = year
        self.odometer_reading : int = 0
    
    def get_descriptive_name(self) -> str:
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage : int):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles : int):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
