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
from application.services.domain import transport_service as ts
from decimal import Decimal
from abc import ABC, abstractmethod
import simplejson as json

class ShippingService():

    @classmethod
    def create_shipping_entity(self, w_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str) -> Shipping:
        try:
            if not isinstance(w_unit, str) or not isinstance(weight_value, Decimal) or not isinstance(distance_unit, str) or not isinstance(distance_value, Decimal) or not isinstance(transport_method, str):
                raise TypeError()

            distance_unit = create_distance_unit(distance_unit)
            weight_unit = create_weight_unit(w_unit)
            transport = ts.create_transport(transport_method)
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
        except Exception as err:
            print(f'an error occured {err}')
    
    @abstractmethod
    def get_estimate_for_shipping(self, data: dict):
        """
        Args:
            api_interface (CarbonInterfaceRequestService): Das API Interface, welches den direkten HTTP-Call an die externe API sendet

        Returns:
            dict: Die Antwortdaten als Python-Datenstruktur (z. B. ein JSON-Objekt).
        """
        pass

    @classmethod
    def convert_shipping_entity_to_json(self, ship: Shipping) -> json:
        return json.dumps({
                "type": ship.type,
                "weight_value": ship.weight_value,
                "weight_unit": ship.weight_unit,
                "distance_value": ship.distance_value,
                "distance_unit": ship.distance_unit,
                "transport_method": ship.transport_method,
                })