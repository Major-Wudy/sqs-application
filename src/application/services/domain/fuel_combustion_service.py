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

class FuelService():
    @classmethod
    def create_fuel_combustion_entity(self, source_type_name: str, consumption_value: Decimal) -> FuelCombustion:
        try:    
            if not isinstance(source_type_name, str) or not isinstance(consumption_value, Decimal):
                raise TypeError()
            
            fuel = FuelSourceType()
            fuel_unit = fuel.get_unit_by_name(source_type_name)
            fuel_api_name = fuel.get_api_name_by_name(source_type_name)

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

    @classmethod
    def convert_fuel_entity_to_json(self, fuel: FuelCombustion) -> json:
        return json.dumps({
                "type": fuel.type,
                "fuel_source_type": fuel.fuel_source_type,
                "fuel_source_unit": fuel.fuel_source_unit,
                "fuel_source_value": fuel.consumption_value
                })

    @abstractmethod
    def get_estimate_for_fuel_use(self, data: dict):
        """
        Args:
            api_interface (CarbonInterfaceRequestService): Das API Interface, welches den direkten HTTP-Call an die externe API sendet

        Returns:
            dict: Die Antwortdaten als Python-Datenstruktur (z. B. ein JSON-Objekt).
        """
        pass