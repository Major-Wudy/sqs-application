import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from models.shipping.shipping import Shipping
from models.shipping.transport import Transport
from models.weights.weight_unit import WeightUnit
from models.activity.activity_type import ActivityType
from services.domain.distance_unit_service import create_distance_unit
from services.domain.weight_unit_service import create_weight_unit
from services.domain.transport_service import create_transport
from decimal import Decimal

def create_shipping_entity(w_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str) -> Shipping:
    try:
        if not isinstance(w_unit, str) or not isinstance(weight_value, Decimal) or not isinstance(distance_unit, str) or not isinstance(distance_value, Decimal) or not isinstance(transport_method, str):
            raise TypeError()

        distance_unit = create_distance_unit(distance_unit)
        weight_unit = create_weight_unit(w_unit)
        transport = create_transport(transport_method)
        return Shipping(ActivityType.SHIPPING, weight_unit, weight_value, distance_unit, distance_value, transport)
    except TypeError:
        if not isinstance(w_unit, str):
            print("w_unit is wrong")
        if not isinstance(weight_value, Decimal):
            print("weight_value is wrong")
        if not isinstance(distance_unit, str):
            print("distance_unit is wrong")
        if not isinstance(distance_value, Decimal):
            print("distance_value is wrong") 
        if not isinstance(transport_method, str):
            print("transport_method is wrong")
        return None