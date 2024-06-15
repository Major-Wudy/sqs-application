import sys
import os
import logging
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.weights.weight_unit import WeightUnit

"""create weight unit entity

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param unit: wight unit you would like
    :type unit: str
    :returns: WeightUnit
    :rtype: WeightUnit
"""
def create_weight_unit(unit: str) -> WeightUnit:
    try:
        if not isinstance(unit, str):
            raise TypeError()

        if unit == "g":
            return WeightUnit.G
        elif unit == "lb":
            return WeightUnit.LB
        elif unit == "kg":
            return WeightUnit.KG
        elif unit == "mt":
            return WeightUnit.MT
        else:
            # Set gramms as default value
            return WeightUnit.G
    except TypeError as err:
        logging.error(f"Default value will be assigned. TypeError raised {err}")
        return WeightUnit.G