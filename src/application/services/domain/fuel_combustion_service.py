import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.activity.activity_type import ActivityType
from application.models.fuel.fuel_combustion import FuelCombustion
from application.models.fuel.fuel_source_type import FuelSourceType
from decimal import Decimal
from abc import ABC, abstractmethod
import simplejson as json

"""Domain Service FuelService

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
"""
class FuelService():
    """create fuel combustion entity

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param consumption_value: Amount of your consumed fuel source
    :type consumption_value: Decimal
    :param source_type_name: name of your fuel source
    :type source_type_name: str
    :param api_unit: corresponding api_unit value
    :type api_unit: str
    :param api_name: corresponding api_name
    :type api_name: str
    :returns: Fuel combustion entity
    :rtype: FuelCombustion or None
    """
    @classmethod
    def create_fuel_combustion_entity(cls, consumption_value: Decimal, source_type_name: str = "", api_unit: str = "", api_name: str = "") -> FuelCombustion | None:
        try:    
            if not isinstance(source_type_name, str) or not isinstance(consumption_value, Decimal):
                raise TypeError()
            
            if api_unit == "" and api_name == "":
                fuel = FuelSourceType()
                fuel_unit = fuel.get_unit_by_name(source_type_name)
                fuel_api_name = fuel.get_api_name_by_name(source_type_name)

            if api_unit != "" and api_name != "":
                fuel_unit = api_unit
                fuel_api_name = api_name

            if fuel_unit == "":
                raise ValueError()
            if fuel_api_name == "":
                raise ValueError()

            return FuelCombustion(ActivityType.FUEL_COMBUSTION, fuel_api_name, fuel_unit, consumption_value)
        except TypeError:
            print("Wrong fuel parameters")
            return None
        except ValueError:
            print("fuel Variables are empty")
            return None
    
    """converts given fuel entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param fuel: fuel entity
    :type fuel: FuelCombustion
    :returns: JSON 
    :rtype: json
    """
    @classmethod
    def convert_fuel_entity_to_json(cls, fuel: FuelCombustion) -> json:
        return {
                "type": fuel.type.value,
                "fuel_source_type": fuel.fuel_source_type,
                "fuel_source_unit": fuel.fuel_source_unit,
                "fuel_source_value": str(fuel.consumption_value)
                }

    """abstract method up for implementation to get estimates from a carbon score api

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param value: Amount of your consumed fuel source
    :type value: Decimal
    :param source_type_name: name of your fuel source
    :type source_type_name: str
    :param api_unit: corresponding api_unit value
    :type api_unit: str
    :param api_name: corresponding api_name
    :type api_name: str
    :returns: server response as json
    """
    @abstractmethod
    def get_estimate_for_fuel_use(self, value: Decimal, source_type_name: str = "", api_unit: str = "", api_name: str = ""):
        pass