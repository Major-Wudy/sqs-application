import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from models.electricity.electricity import Electricity
from models.electricity.electricity_unit import ElectricityUnit
from models.activity.activity_type import ActivityType
from decimal import Decimal

def create_electricity_entity(consumption_value: Decimal, country: str, state: str) -> Electricity:
    elec = Electricity(ActivityType.ELECTRICITY, consumption_value, country, state)
    return elec

def get_estimate_for_electricity_use(cirs, elec: Electricity) -> Electricity:
    return elec

def change_electricity_unit(elec: Electricity, unit: ElectricityUnit):
    try:
        if not isinstance(elec, Electricity) or not isinstance(unit, ElectricityUnit):
            raise TypeError()
        elec.electricity_unit = unit
    except TypeError:
        print("Wrong parameters")
