import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from models.distance.distance_unit import distance_unit

def create_distance_unit(unit: str) -> distance_unit:
    try:
        if not isinstance(unit, str):
            raise TypeError()

        if unit == "km":
            return distance_unit.KM
        elif unit == "mi":
            return distance_unit.MI
        else:
            # Set Km as default value
            return distance_unit.KM
    except TypeError:
        print("Wrong parameters")