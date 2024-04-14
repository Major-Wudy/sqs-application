import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

from infrastructure.carbon_interface_api import CarbonInterfaceRequestService
from services.domain.electricity_service import ElectricityService
from decimal import Decimal
import requests
import simplejson as json

class EstimatesService(CarbonInterfaceRequestService, ElectricityService):
    def post(self, url: str, data: dict = None, json: dict = None, headers: dict = None) -> dict:
        try:
            if url == None or url == "":
                raise ValueError()
            
            if headers == None and data == None and json == None:
                response = requests.post(url)
            if headers != None and data == None and json == None:
                response = requests.post(url, headers=headers)
            if headers != None and data != None and json == None:
                response = requests.post(url, data=data, headers=headers)
                print(data)
            if headers != None and data != None and json != None:
                response = requests.post(url, headers=headers, data=data, json=json)
            if headers == None and data != None and json == None:
                response = requests.post(url, data=data)
            if headers == None and data != None and json != None:
                response = requests.post(url, data=data, json=json)
            if headers == None and data == None and json != None:
                response = requests.post(url, json=json)
            if headers != None and data == None and json != None:
                response = requests.post(url, headers=headers, json=json)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        except ValueError as ve:
            print(f'Value error occured: {ve}')
        else:
            print(response.text)

    def get_estimate_for_electricity_use(self, data: dict):
        try:
            es = ElectricityService()
            elec = es.create_electricity_entity(Decimal(data.get('value')), data.get('country'), data.get('state'), data.get('unit'))
            
            url = self.get_estimates_url()
            headers = self.get_authorization_and_content_type_header()
            
            payload = 
            
            self.post(url, data=payload, headers=headers)
        except Exception as err:
            print(f'An error occurred: {err}')