import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.distance.distance_unit import DistanceUnit

def create_distance_unit(unit: str) -> DistanceUnit:
    try:
        if not isinstance(unit, str):
            raise TypeError()

        if unit == "km":
            return DistanceUnit.KM
        elif unit == "mi":
            return DistanceUnit.MI
        else:
            # Set Km as default value
            return DistanceUnit.KM
    except TypeError:
        return DistanceUnit.KM