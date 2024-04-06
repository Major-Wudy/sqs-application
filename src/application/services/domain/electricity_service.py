import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from models.electricity.electricity import electricity
from models.electricity.electricity_unit import electricity_unit
from models.activity.activity_type import activity_type
from decimal import Decimal

def create_electricity_entity(type: activity_type, consumption_value: Decimal, country: str, state: str) -> electricity:
    elec = electricity(type, consumption_value, country, state)
    return elec

def get_estimate_for_electricity_use(cirs, elec: electricity) -> electricity:
    return elec

def change_electricity_unit(elec: electricity, unit: electricity_unit):
    try:
        if not isinstance(elec, electricity) or not isinstance(unit, electricity_unit):
            raise TypeError()
        elec.electricity_unit = unit
    except TypeError:
        print("Wrong parameters")

# Testing Code Section

elec = create_electricity_entity(activity_type.ELECTRICITY, 105.5, "Germany", "Bavaria")
print(elec.type)
