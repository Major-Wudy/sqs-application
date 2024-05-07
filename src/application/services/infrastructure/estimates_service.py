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

class EstimatesService(CarbonInterfaceRequestService, ElectricityService, FlightService, ShippingService, FuelService):
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
    
    def get_estimate_for_flight(self, passengers: int, depature: str, destination: str, unit: str, cabin: str):
        try:
            fs = FlightService()
            fl = fs.create_flight_entity(passengers, depature, destination, unit, cabin)

            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
            
            payload = fs.convert_flight_entity_to_json(fl)

            return self.post(url, data=payload, headers=headers)
        except Exception as err:
            return {'error': f'Please check params. Error message {err}'}
    
    def get_estimate_for_shipping(self, weight_unit: str, weight_value: Decimal, distance_unit: str, distance_value: Decimal, transport_method: str):
        try:
            ship_s = ShippingService()
            ship = ship_s.create_shipping_entity(weight_unit, weight_value, distance_unit, distance_value, transport_method)

            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
        
            payload = ship_s.convert_shipping_entity_to_json(ship)

            return self.post(url, data=payload, headers=headers)
        except Exception as err:
            return {'error': f'Please check params. Error message {err}'}

    def get_estimate_for_fuel_use(self, source_type_name: str, value: Decimal): 
        try:
            fs = FuelService()
            fuel = fs.create_fuel_combustion_entity(source_type_name, Decimal('value'))

            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
        
            payload = fs.convert_fuel_entity_to_json(fuel)

            return self.post(url, data=payload, headers=headers)
        except Exception as err:
            return {'error': f'Please check params. Error message {err}'}