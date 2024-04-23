from decimal import Decimal

class Shipping:
    def __init__(self, type, weight_unit, weight_value, distance_unit, distance_value, transport_method):
            self.type = type
            self.weight_unit = weight_unit
            self.weight_value = weight_value
            self.distance_unit = distance_unit
            self.distance_value = distance_value
            self.transport_method = transport_method
             