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

def create_fuel_combustion_entity(source_type_name: str, consumption_value: Decimal) -> FuelCombustion:
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