from CabinClass import *

class Leg:
    def __init__(self, depature_airport: str, destination_airport: str, cabin_class: CabinClass):
        try:
            if not isinstance(depature_airport, str) or not isinstance(destination_airport, str) or not isinstance(cabin_class, CabinClass):
                raise TypeError()
            self.depature_airport = depature_airport
            self.destination_airport = destination_airport
            self.cabin_class = cabin_class
        except TypeError:
            print("Could not create Leg Object")
            print("parameters are not the correct type")
            print("depature_airport, destination_airport must be str and cabin_class must be CabinClass")