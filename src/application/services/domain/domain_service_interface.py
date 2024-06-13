import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.services.domain.electricity_service import ElectricityService
from application.services.domain.flight_service import FlightService
from application.models.electricity.electricity import Electricity
from application.models.electricity.electricity_unit import ElectricityUnit
from application.models.activity.activity_type import ActivityType
from decimal import Decimal
from abc import ABC, abstractmethod
import simplejson as json

class DomainServiceInterface(ElectricityService):

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
    def create_electricity_entity(self, consumption_value: Decimal, country: str, state: str, unit: str = ElectricityUnit.KWH) -> Electricity:
        if unit != None:
            elec = Electricity(ActivityType.ELECTRICITY, consumption_value, country, state)
        if unit == None:
            elec = Electricity(ActivityType.ELECTRICITY, consumption_value, country, state, unit)
        return elec

    """prepare electricity entity for api call

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param value: consumed electricity value
    :type value: Decimal
    :param country: country you are located in or want to know the carbon scores for
    :type country: str
    :param state: state you are located in or want to know the carbon scores for
    :type state: str
    :param unit: electricity unit kwh or mwh
    :type unit: str
    :returns: Json of electricity entity
    """
    def prepare_electricity_for_estimate(self, value: Decimal, country: str, state: str, unit: str) -> json:
        elec = self.create_electricity_entity(Decimal(value), country, state, unit)

        es = ElectricityService()
        payload = es.convert_electricity_entity_to_json(elec)
        return payload

    """changes electricity unit for given electricity entity

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param elec: Electricity entity for changing the electricity unit
    :type elec: Electricity
    :param unit: Electricity unit you want kwh or mwh
    :type unit: ElectricityUnit
    """
    def change_electricity_unit(self, elec: Electricity, unit: ElectricityUnit):
        es = ElectricityService()
        es.change_electricity_unit(elec, unit)


    """converts given electricity Entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param elec: Electricity entity
    :type elec: Electricity
    :returns: JSON 
    :rtype: json
    """
    def convert_electricity_entity_to_json(cls, elec: Electricity) -> json:
        es = ElectricityService()
        return es.convert_electricity_entity_to_json(elec)
