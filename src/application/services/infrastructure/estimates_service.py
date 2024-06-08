import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from application.services.infrastructure.carbon_interface_api import CarbonInterfaceRequestService
from application.services.domain.electricity_service import ElectricityService
from application.services.domain.flight_service import FlightService
from application.services.domain.shipping_service import ShippingService
from application.services.domain.fuel_combustion_service import FuelService
from decimal import Decimal
import requests
import simplejson

"""Infrastructure Service EstimatesService

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param CarbonInterfaceRequestService: Used API Interface class
    :type CarbonInterfaceRequestService: CarbonInterfaceRequestService
    :param ElectricityService: Domain Service to access all functionalities around electricity
    :type ElectricityService: ElectricityService
    :param FlightService: Domain Service to access all functionalities around flights
    :type: FlightService: FlightService
    :param ShippingService: Domain Service to access all functionalities around shipping
    :type ShippingService: ShippingService
    :param FuelService: Domain Service to access all functionalities around fuel consumption
    :type FuelService: FuelService
"""
class EstimatesService(CarbonInterfaceRequestService, ElectricityService, FlightService, ShippingService, FuelService):
    """Post some data against url

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param url: url you want to post against
        :type url: str
        :param data: contains data as dictionary you want to post
        :type data: dict
        :param json: contains json data you want to post
        :type json: dict
        :param headers: contains http headers you want to use
        :type headers: dict
        :returns: server response as json
        :rtype: dict
    """
    def post(self, url: str, data: dict = None, json: dict = None, headers: dict = None) -> dict:
        try:
            if url == None or url == "":
                raise ValueError()

            request_args = {'url': url}
            if headers is not None:
                request_args['headers'] = headers
            if data is not None:
                request_args['data'] = data
            if json is not None:
                request_args['json'] = json
            
            response = requests.post(**request_args)
            response.raise_for_status()

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            message = request_args
            return {'error': f'HTTP error occurred: {http_err}. {message}'}
        except Exception as err:
            return {'error': f'something went wrong {err}. Url provided?'}
        else:
            print(response.json())

    """get estimate for electricity use

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param value: electricity consumption value
        :type value: Decimal
        :param country: the choosen country you want to get your estimates for. official abbreviation
        :type country: str
        :param state: to be specific. the choosen state you want to get your estimates for. offical abbreviation
        :type state: str
        :param unit: Which electricity unit do you want? kwh or mwh
        :type unit: str
        :returns: server response as json
        :rtype: dict
    """
    def get_estimate_for_electricity_use(self, value: Decimal, country: str, state: str, unit: str):
        try:
            es = ElectricityService()
            elec = es.create_electricity_entity(Decimal(value), country, state, unit)
            
            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
            
            payload = es.convert_electricity_entity_to_json(elec)
            return self.post(url, json=payload, headers=headers)
        except Exception as err:
            return {'error': f'Please check params. Error message {err}'}
    
    """get estimate for your flight

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param passengers: Amount of passengers for your estimation
        :type passengers: int
        :param depature: Airport from which you are departing. official abbreviation
        :type depature: str
        :param destination: Airport where you arrive. offical abbreviation
        :type destination: str
        :param unit: distance unit you want your estimation based on km or mi
        :type unit: str
        :param cabin: Cabin class economy or premium
        :type cabin: str
        :returns: server response as json
        :rtype: dict
    """
    def get_estimate_for_flight(self, passengers: int, depature: str, destination: str, unit: str, cabin: str):
        try:
            fs = FlightService()
            fl = fs.create_flight_entity(passengers, depature, destination, unit, cabin)
            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
            
            payload = fs.convert_flight_entity_to_json(fl)

            return self.post(url, json=payload, headers=headers)
        except Exception as err:
            return {'error': f'Please check params. Error message {err}'}
    
    """get estimate for package shipping

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param weight_unit: Unit of your package weight g, kg, lb, mt
        :type weight_unit: str
        :param weight_value: Weight of your package 
        :type weight_value: Decimal
        :param distance_unit: Unit you want your estimate be based on km or mi
        :type distance_unit: str
        :param distance_value: Distance of your shipping route
        :type distance_value: Decimal
        :param transport_methid: Method of shipping your package. Truck, trian, plane, ship
        :type transport_method: str
        :returns: server response as json
        :rtype: dict
    """
    def get_estimate_for_shipping(self, weight_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str):
        try:
            ship_s = ShippingService()
            ship = ship_s.create_shipping_entity(weight_unit, weight_value, distance_unit, distance_value, transport_method)

            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
        
            payload = ship_s.convert_shipping_entity_to_json(ship)

            return self.post(url, json=payload, headers=headers)
        except Exception as err:
            return {'error': f'Please check params. Error message {err}'}

    """get estimate for fuel consumption

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param value: Amount of fuel consumed
        :type value: Decimal
        :param source_type_name: name of your fuel source 
        :type source_type_name: str
        :param api_unit: api unit of fuel source
        :type api_unit: str
        :param api_name: api name of fuel source
        :type api_name: str
        :returns: server response as json
        :rtype: dict
    """
    def get_estimate_for_fuel_use(self, value: Decimal, source_type_name: str = "", api_unit: str = "", api_name: str = ""): 
        try:
            fs = FuelService()
            if source_type_name == "":
                fuel = fs.create_fuel_combustion_entity(value, "", api_unit, api_name)

            if api_unit == "" and api_name == "":
                fuel = fs.create_fuel_combustion_entity(value, source_type_name)

            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
        
            payload = fs.convert_fuel_entity_to_json(fuel)

            return self.post(url, json=payload, headers=headers)
        except Exception as err:
            return {'error': f'Please check params. Error message {err}'}