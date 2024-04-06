from decimal import Decimal
from models.electricity.electricity_unit import electricity_unit

class electricity:
    def __init__(self, type, electricity_value, country, state, electricity_unit=electricity_unit.KWH):
        self.type = type
        self.electricity_value = Decimal(electricity_value)
        self.country = country
        self.state = state
        self.electricity_unit = electricity_unit