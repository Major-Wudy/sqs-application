import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.shipping.shipping import Shipping
from application.models.shipping.transport import Transport
from application.models.weights.weight_unit import WeightUnit
from application.models.activity.activity_type import ActivityType
from application.services.domain.distance_unit_service import create_distance_unit
from application.services.domain.weight_unit_service import create_weight_unit
from application.services.domain.transport_service import create_transport
from decimal import Decimal
from abc import ABC, abstractmethod
import simplejson as json

"""Domain Service ShippingService

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
"""
class ShippingService():
    """create shipping entity 

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param w_unit: weight unit of your package g, kg, lb, mt
    :type w_unit: str
    :param weight_value: weight of your package corresponding to your choosen w_unit
    :type weight_value: Decimal
    :param distance_unit: prefered distance unit km or mi
    :type distance_unit: str
    :param distance_value: corresponding distance
    :type distance_value: Decimal
    :param transport_method: How do you want your package shipped? Train, truck, plane, ship
    :type transport_method: str
    :returns: Shipping entity or nothing
    :rtype: Shippung or None
    """
    @classmethod
    def create_shipping_entity(cls, w_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str) -> Shipping | None:
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
        except Exception as err:
            print(f'an error occured {err}')
    
    """abstract method up for implementation to get estimates form a carbon score api

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param weight_unit: weight unit of your package g, kg, lb, mt
    :type weight_unit: str
    :param weight_value: weight of your package corresponding to your choosen w_unit
    :type weight_value: Decimal
    :param distance_unit: prefered distance unit km or mi
    :type distance_unit: str
    :param distance_value: corresponding distance
    :type distance_value: Decimal
    :param transport_method: How do you want your package shipped? Train, truck, plane, ship
    :type transport_method: str
    :returns: server response as json
    """
    @abstractmethod
    def prepare_for_shipping_estimate(self, weight_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str):
        pass

    """converts shipping entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param ship: shipping entity
    :type ship: Shipping
    :returns: shipping entity as json
    :rtype: json
    """
    @classmethod
    def convert_shipping_entity_to_json(cls, ship: Shipping) -> json:
        return {
                "type": ship.type.value,
                "weight_value": str(ship.weight_value),
                "weight_unit": ship.weight_unit.value,
                "distance_value": str(ship.distance_value),
                "distance_unit": ship.distance_unit.value,
                "transport_method": ship.transport_method.value,
                }