from decimal import Decimal
import models.electricity.electricity_unit as eu
# Negativ Beispiel
#import application.services.domain.electricity_service as es
from application.services.domain import electricity_service as es

class Electricity:
    def __init__(self, type, electricity_value, country, state, electricity_unit=eu.ElectricityUnit.KWH):
        self.type = type
        self.electricity_value = Decimal(electricity_value)
        self.country = country
        self.state = state
        self.electricity_unit = electricity_unit