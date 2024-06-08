import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.electricity.electricity import Electricity
from application.models.electricity.electricity_unit import ElectricityUnit
from application.models.activity.activity_type import ActivityType
from decimal import Decimal
from abc import ABC, abstractmethod
import simplejson as json

"""Domain Service ElectricityService

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
"""
class ElectricityService():
    """creates electricity entity

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param consumption_valule: consumed electricity value
    :type consumption_value: Decimal
    :param country: country you are located in or want to know the carbon scores for
    :type country: str
    :param state: state you are located in or want to know the carbon scores for
    :type state: str
    :param unit: electricity unit kwh or mwh
    :type unit: str
    :returns: Electricity entity
    :rtype: Electricity
    """
    @classmethod
    def create_electricity_entity(cls, consumption_value: Decimal, country: str, state: str, unit: str = ElectricityUnit.KWH) -> Electricity:
        if unit != None:
            elec = Electricity(ActivityType.ELECTRICITY, consumption_value, country, state)
        if unit == None:
            elec = Electricity(ActivityType.ELECTRICITY, consumption_value, country, state, unit)
        return elec

    """changes electricity unit for given electricity entity

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param elec: Electricity entity for changing the electricity unit
    :type elec: Electricity
    :param unit: Electricity unit you want kwh or mwh
    :type unit: ElectricityUnit
    """
    @classmethod
    def change_electricity_unit(cls, elec: Electricity, unit: ElectricityUnit):
        try:
            if not isinstance(elec, Electricity) or not isinstance(unit, ElectricityUnit):
                raise TypeError()
            elec.electricity_unit = unit
        except TypeError:
            print("Wrong elec parameters")

    """converts given electricity Entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param elec: Electricity entity
    :type elec: Electricity
    :returns: JSON 
    :rtype: json
    """
    @classmethod
    def convert_electricity_entity_to_json(cls, elec: Electricity) -> json:
        value = elec.electricity_value
        return {
                "type": elec.type.value,
                "electricity_unit": elec.electricity_unit.value,
                "electricity_value": str(value),
                "country": elec.country,
                "state": elec.state,
                }

    """abstract method up for implementation to get estimates from a carbon score api

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param value: consumed electricity value
    :type value: Decimal
    :param country: country you are located in or want to know the carbon scores for
    :type country: str
    :param state: state you are located in or want to know the carbon scores for
    :type state: str
    :param unit: electricity unit kwh or mwh
    :type unit: str
    :returns: Server Response as Json
    """
    @abstractmethod
    def get_estimate_for_electricity_use(self, value: Decimal, country: str, state: str, unit: str):
        pass

