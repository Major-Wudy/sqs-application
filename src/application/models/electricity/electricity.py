from decimal import Decimal
from application.models.electricity.electricity_unit import ElectricityUnit

class Electricity:
    def __init__(self, type, electricity_value, country, state, electricity_unit=ElectricityUnit.KWH):
        self.type = type
        self.electricity_value = Decimal(electricity_value)
        self.country = country
        self.state = state
        self.electricity_unit = electricity_unit

    def __json__(self):
        return {'data': self.data}