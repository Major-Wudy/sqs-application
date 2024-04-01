from ActivityType import *
from ElectricityUnit import *
from decimal import Decimal

class Electricity:
    def __init__(self, type, electricity_unit, electricity_value, country, state):
        self.type = type
        self.electricity_unit = electricity_unit
        self.electricity_value = Decimal(electricity_value)
        self.country = country
        self.state = state

"""

"""