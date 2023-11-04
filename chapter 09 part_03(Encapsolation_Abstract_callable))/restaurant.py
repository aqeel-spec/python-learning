# code from previous exercise 9-4
class Resturants(): # () -> used in latest python but : -> used in old python 

    # initialize the __init__() method for resturants
    def __init__(self, resturant_name : str,cuisine_type: str):
        # two attributes having name resturant_name and cuisine_type
        self.resturant_name : str  = resturant_name
        self.cuisine_type : str = cuisine_type
        self.number_served : int = 0
    
    # describe method to show above attributes
    def describe_resturant(self):
        print(f"The name of the resturant is ((({self.resturant_name}))) and the cuisine type is (({self.cuisine_type}))")
    
    def open_resturant(self):
        print(f"(({self.resturant_name})) is open now")
    
    # method set_number_served
    def set_number_served(self, number_served : int):
        self.number_served = number_served

    # decreament method that let you increament the no of customers
    def increament_number_served(self, increament : int):
        self.number_served += increament