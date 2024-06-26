import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.services.domain.electricity_service import ElectricityService
from application.services.domain.flight_service import FlightService
from application.services.domain.shipping_service import ShippingService
from application.services.domain.fuel_combustion_service import FuelService
from application.services.domain.carbon_service import CarbonService

from decimal import Decimal
from abc import ABC, abstractmethod
import simplejson as json

class DomainServiceInterface(ElectricityService, FlightService, ShippingService, FuelService, CarbonService):

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
    def create_electricity_entity(self, consumption_value: Decimal, country: str, state: str, unit: str = ""):
        es = ElectricityService()
        return es.create_electricity_entity(consumption_value, country, state, unit)

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
    def change_electricity_unit(self, elec, unit):
        es = ElectricityService()
        es.change_electricity_unit(elec, unit)


    """converts given electricity Entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param elec: Electricity entity
    :type elec: Electricity
    :returns: JSON 
    :rtype: json
    """
    def convert_electricity_entity_to_json(self, elec) -> json:
        es = ElectricityService()
        return es.convert_electricity_entity_to_json(elec)


    """create flight entity

        :author: Raphael Wudy (raphael.wudy@stud.th-rosensehim.de)
        :param passengers: amount of passengers
        :type passengers: int
        :param departure:  Airport from which you are departing. International abbreviation Dublin equals DUB
        :type departure: str
        :param destination: Airport where you arrive. International abbreviation Munich equals MUC
        :type destination: str 
        :param distance_unit: the distance unit you want your estimates be based on km or mi 
        :type distance_unit: str
        :param cabin: Cabin class economy or premium
        :type cabin: str
        :returns: Flight entity
    """
    def create_flight_entity(self, passengers: int, departure: str, destination: str, distance_unit: str, cabin: str):
        fs = FlightService()
        return fs.create_flight_entity(passengers, departure, destination, distance_unit, cabin)

    """create needed leg object for your flight entity. containing destination and departure airports and choosen cabin class

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param departure: Airport from which you are departing. International abbreviation Dublin equals DUB
    :type departure: str
    :param destination: Airport where you arrive. International abbreviation Munich equals MUC
    :type destination: str
    :param cabin: Cabin class you intending to book
    :type cabin: str
    :returns: Leg entity containing destination and departure Airports and cabin class  
    """
    def create_leg_object(self, departure: str, destination: str, cabin: str):
        fs = FlightService()
        return fs.create_leg_object(departure, destination, cabin)

    """get cabin class from given string value

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param type: Choosen cabin class for your flight
    :type type: str
    :returns: Cabin class economy or premium
    """
    def get_cabin_class(self, type: str):
        fs = FlightService()
        return fs.get_cabin_class(type)

    """abstract method up for implementation to get estimates from a carbon score api

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param passangers: Amount of passengers
    :type passengers: int
    :param departure:  Airport from which you are departing. International abbreviation Dublin equals DUB
    :type departure: str
    :param destination: Airport where you arrive. International abbreviation Munich equals MUC
    :type destination: str 
    :param unit: the distance unit you want your estimates be based on km or mi 
    :type unit: str
    :param cabin: Cabin class economy or premium
    :type cabin: str
    :returns: json flight entity
    :rtype: json
    """
    def prepare_flight_for_estimate(self, passengers: int, departure: str, destination: str, unit: str, cabin: str) -> json:
       fl = self.create_flight_entity(passengers, departure, destination, unit, cabin)
       return self.convert_flight_entity_to_json(fl)

    """converts given flight entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param flight: Flight entity
    :type flight: flight
    :returns: JSON 
    :rtype: json
    """
    def convert_flight_entity_to_json(self, flight) -> json:
        fs = FlightService()
        return fs.convert_flight_entity_to_json(flight)

    """Helper function for possible ui implementation 

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :returns: IATA URL for official international airport abbreviations
    :rtype: str
    """
    def iata_airport_info_url(self) -> str:
        fs = FlightService()
        return fs.iata_airport_info_url()

    """create shipping entity 

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param w_unit: weight unit of your package g, kg, lb, mt
    :type w_unit: str
    :param weight_value: weight of your package corresponding to your choosen w_unit
    :type weight_value: Decimal
    :param distance_unit: prefered distance unit km or mi
    :type distance_unit: str
    :param distance_value: corresponding distance
    :type distance_value: Decimal
    :param transport_method: How do you want your package shipped? Train, truck, plane, ship
    :type transport_method: str
    :returns: Shipping entity or nothing
    """
    def create_shipping_entity(self, w_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str):
        s = ShippingService()
        return s.create_shipping_entity(w_unit, weight_value, distance_unit, distance_value, transport_method)

    """prepare shipping entity for estimates form a carbon score api

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param weight_unit: weight unit of your package g, kg, lb, mt
    :type weight_unit: str
    :param weight_value: weight of your package corresponding to your choosen w_unit
    :type weight_value: Decimal
    :param distance_unit: prefered distance unit km or mi
    :type distance_unit: str
    :param distance_value: corresponding distance
    :type distance_value: Decimal
    :param transport_method: How do you want your package shipped? Train, truck, plane, ship
    :type transport_method: str
    :returns: json shipping entity
    :rtype: json
    """
    def prepare_for_shipping_estimate(self, weight_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str) -> json:
        ship = self.create_shipping_entity(weight_unit, weight_value, distance_unit, distance_value, transport_method)
        return self.convert_shipping_entity_to_json(ship)

    """converts shipping entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param ship: shipping entity
    :type ship: Shipping
    :returns: shipping entity as json
    :rtype: json
    """
    def convert_shipping_entity_to_json(self, ship) -> json:
        s = ShippingService()
        return s.convert_shipping_entity_to_json(ship)

    """create fuel combustion entity

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param consumption_value: Amount of your consumed fuel source
    :type consumption_value: Decimal
    :param source_type_name: name of your fuel source
    :type source_type_name: str
    :param api_unit: corresponding api_unit value
    :type api_unit: str
    :param api_name: corresponding api_name
    :type api_name: str
    :returns: Fuel combustion entity
    """
    def create_fuel_combustion_entity(self, consumption_value: Decimal, source_type_name: str = "", api_unit: str = "", api_name: str = ""):
        fs = FuelService()
        return fs.create_fuel_combustion_entity(consumption_value, source_type_name, api_unit, api_name)

    """converts given fuel entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param fuel: fuel entity
    :type fuel: FuelCombustion
    :returns: JSON 
    :rtype: json
    """
    def convert_fuel_entity_to_json(self, fuel) -> json:
        fs = FuelService()
        return fs.convert_fuel_entity_to_json(fuel)

    """abstract method up for implementation to get estimates from a carbon score api

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param value: Amount of your consumed fuel source
    :type value: Decimal
    :param source_type_name: name of your fuel source
    :type source_type_name: str
    :param api_unit: corresponding api_unit value
    :type api_unit: str
    :param api_name: corresponding api_name
    :type api_name: str
    :returns: server response as json
    """
    def prepare_fuel_for_estimate(self, value: Decimal, source_type_name: str = "", api_unit: str = "", api_name: str = ""):
        if source_type_name == "":
            fuel = self.create_fuel_combustion_entity(value, "", api_unit, api_name)

        if api_unit == "" and api_name == "":
            fuel = self.create_fuel_combustion_entity(value, source_type_name)
        return self.convert_fuel_entity_to_json(fuel)

    """create carbon score entity

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param score_g: estimated carbon score in gramms
        :type score_g: Decimal
        :param score_kg: estimated carbon score in kilo gramms
        :type score_kg: Decimal
        :param score_lb: estimated carbon score in pounds
        :type score_lb: Decimal
        :param score_mt: estimated carbon score in mega tons
        :type score_mt: Decimal
        :param session_id: user session id or auth token
        :type session_id: str
        :returns: Score
        :rtype: Score
    """
    def create_carbon_score(self, score_g: Decimal, score_kg: Decimal, score_lb: Decimal, score_mt: Decimal, session_id: str):
        cs = CarbonService()
        return cs.create_carbon_score(score_g, score_kg, score_lb, score_mt, session_id)

    """converts given Carbon Score Entity to json

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param score: Score entity
        :type score: Score
        :returns: dictionary
        :rtype: dict
    """
    def convert_score_to_json(self, score) -> dict:
        cs = CarbonService()
        return cs.convert_score_to_json(score)