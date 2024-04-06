import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from models.shipping.shipping import shipping
from models.shipping.transport import transport
from models.weights.weight_unit import weight_unit
from models.activity.activity_type import activity_type
from services.domain.distance_unit_service import create_distance_unit
from decimal import Decimal

def create_shipping_entity(type: activity_type, w_unit: weight_unit, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: transport) -> shipping:
    try:
        if not isinstance(type, activity_type) or not isinstance(w_unit, weight_unit) or not isinstance(weight_value, Decimal) or not isinstance(distance_unit, str) or not isinstance(distance_value, Decimal) or not isinstance(transport_method, transport):
            raise TypeError()

        distance_unit = create_distance_unit(distance_unit)
        return shipping(type, w_unit, weight_value, distance_unit, distance_value, transport_method)
    except TypeError:
        if not isinstance(type, activity_type): 
            print("activity_type is wrong")
        if not isinstance(w_unit, weight_unit):
            print("w_unit is wrong")
        if not isinstance(weight_value, Decimal):
            print("weight_value is wrong")
        if not isinstance(distance_unit, str):
            print("distance_unit is wrong")
        if not isinstance(distance_value, Decimal):
            print("distance_value is wrong") 
        if not isinstance(transport_method, transport):
            print("transport_method is wrong")

"""
ship = create_shipping_entity(activity_type.SHIPPING, weight_unit.KG, Decimal("100.5"), "mi", Decimal("110.5"), transport.TRUCK)
print(ship.type)
print(ship.weight_unit)
print(ship.weight_value)
print(ship.distance_unit)
print(ship.distance_value)
print(ship.transport_method)
"""