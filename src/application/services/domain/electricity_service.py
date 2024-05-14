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

class ElectricityService():
    @classmethod
    def create_electricity_entity(cls, consumption_value: Decimal, country: str, state: str, unit: str = ElectricityUnit.KWH) -> Electricity:
        if unit != None:
            elec = Electricity(ActivityType.ELECTRICITY, consumption_value, country, state)
        if unit == None:
            elec = Electricity(ActivityType.ELECTRICITY, consumption_value, country, state, unit)
        return elec

    @classmethod
    def change_electricity_unit(cls, elec: Electricity, unit: ElectricityUnit):
        try:
            if not isinstance(elec, Electricity) or not isinstance(unit, ElectricityUnit):
                raise TypeError()
            elec.electricity_unit = unit
        except TypeError:
            print("Wrong elec parameters")

    def convert_electricity_entity_to_json(self, elec: Electricity) -> json:
        value = elec.electricity_value
        return {
                "type": elec.type.value,
                "electricity_unit": elec.electricity_unit.value,
                "electricity_value": str(value),
                "country": elec.country,
                "state": elec.state,
                }

    @abstractmethod
    def get_estimate_for_electricity_use(self, value: Decimal, country: str, state: str, unit: str):
        """
        Args:
            api_interface (CarbonInterfaceRequestService): Das API Interface, welches den direkten HTTP-Call an die externe API sendet

        Returns:
            dict: Die Antwortdaten als Python-Datenstruktur (z. B. ein JSON-Objekt).
        """
        pass

