from FuelSourceType import *

class FuelCombustion:
    def __init__(self, type, fuelSource_type, fuelSource_unit, consumptionValue):
        self.type = type
        self.fuelSource_type = fuelSource_type
        self.fuelSource_unit = fuelSource_unit
        self.consumptionValue = consumptionValue
