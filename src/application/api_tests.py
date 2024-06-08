import random
import unittest
import sys
import os
import django
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(current_dir)
sys.path.append(parent_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'carbonscore.settings'

# Automated API Tests
from django.test import Client
from dotenv import load_dotenv
import simplejson as json
import requests
class ApiTestCase(unittest.TestCase):
    django.setup()
    token = os.environ.get('TOKEN_UNIT_TEST')
    c = Client()
    electricity_endpoint = "/api/create/electricity/"
    flight_endpoint = "/api/create/flight/"
    shipping_endpoint = "/api/create/shipping/"
    fuel_endpoint = "/api/create/fuel/"
    estimate_electricity_endpoint = "/api/get/estimate/electricity/"
    estimate_flight_endpoint = "/api/get/estimate/flight/"
    estimate_shipping_endpoint = "/api/get/estimate/shipping/"
    estimate_fuel_endpoint = "/api/get/estimate/fuel/"

    header = {'Authorization': 'Bearer ' + token}

    def test_api_create_electricity(self):
        response = self.c.post(self.electricity_endpoint, {"value":123.45, "country":"us","state":"fl","unit":"kwh"}, headers=self.header)
        status_code = response.status_code
        json = response.json()
        self.assertEqual(status_code, 201)
        self.assertIsInstance(json, dict)
        self.assertEqual(json.get('type'), "electricity")
        self.assertEqual(json.get('electricity_unit'), "kwh")
        self.assertEqual(json.get('electricity_value'), "123.45")
        self.assertEqual(json.get('country'), "us")
        self.assertEqual(json.get('state'), "fl")
    
    def test_api_create_electricity_401(self): 
        response = self.c.post(self.electricity_endpoint, {"value":123.45, "country":"us","state":"fl","unit":"kwh"})
        status_code = response.status_code
        self.assertEqual(status_code, 401)
    
    
    def test_api_create_electricity_estimate(self):
        json_data ={"type": "electricity", "electricity_unit": "kwh", "electricity_value": "1650", "country": "us", "state": "fl"}
        
        result = self.c.post(self.estimate_electricity_endpoint, json_data, headers=self.header)
        result_json = result.json()
        data = result_json.get('data')
        attributes = data.get('attributes')
        status_code = result.status_code
        self.assertEqual(status_code, 201)
        self.assertEqual(attributes.get('country'), 'us')
        self.assertEqual(attributes.get('state'), 'fl')
        self.assertEqual(attributes.get('electricity_unit'), 'kwh')
        self.assertEqual(attributes.get('electricity_value'), 123.45)

    def test_api_create_electricity_500(self):
        response = self.c.post(self.electricity_endpoint, {"value":"test", "country":"us","state":"fl","unit":"kwh"}, headers=self.header)
        status_code = response.status_code
        self.assertEqual(status_code, 500)

    # Api test flight
    def test_api_create_flight(self):
        response = self.c.post(self.flight_endpoint, {"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}, headers=self.header, content_type='application/json')
        status_code = response.status_code
        result = response.json()
        self.assertEqual(status_code, 201)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('type'), "flight")
        self.assertEqual(result.get('passengers'), "2")
        self.assertEqual(result.get('legs')[0]["departure_airport"], "MUC")
        self.assertEqual(result.get('legs')[0]['destination_airport'], "DUB")
        self.assertEqual(result.get('legs')[0]['cabin_class'], "premium")
        self.assertEqual(result.get('distance_unit'), "km")
    
    def test_api_create_flight_401(self): 
        response = self.c.post(self.flight_endpoint, {"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"})
        status_code = response.status_code
        self.assertEqual(status_code, 401)

    
    # Api test shipping
    def test_api_create_shipping(self):
        response = self.c.post(self.shipping_endpoint, {"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}, headers=self.header, content_type='application/json')
        status_code = response.status_code
        result = response.json()
        self.assertEqual(status_code, 201)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('type'), "shipping")
        self.assertEqual(result.get('weight_value'), "123.45")
        self.assertEqual(result.get('weight_unit'), "g")
        self.assertEqual(result.get('distance_value'), "500.01")
        self.assertEqual(result.get('distance_unit'), "km")
        self.assertEqual(result.get('transport_method'), "plane")
    
    def test_api_create_shipping_401(self): 
        response = self.c.post(self.shipping_endpoint, {"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"})
        status_code = response.status_code
        self.assertEqual(status_code, 401)
   
    def test_api_create_shipping_500(self):
        response = self.c.post(self.shipping_endpoint, {"weight_value":"error","weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}, headers=self.header)
        status_code = response.status_code
        self.assertEqual(status_code, 500)

    def test_api_create_shipping_estimate(self):
        json_data = {"type": "shipping","weight_value": "123.45","weight_unit": "g","distance_value": "500.01","distance_unit": "km","transport_method": "plane"}
        
        result = self.c.post(self.estimate_shipping_endpoint, json_data, headers=self.header)
        result_json = result.json()
        data = result_json.get('data')
        attributes = data.get('attributes')
        status_code = result.status_code
        self.assertEqual(status_code, 201)
        self.assertEqual(attributes.get('weight_unit'), "g")
        self.assertEqual(attributes.get('weight_value'), 123.45)
        self.assertEqual(attributes.get('distance_value'), 500.01)
        self.assertEqual(attributes.get('distance_unit'), "km")

    # Api test fuel
    def test_api_create_fuel(self):
        response = self.c.post(self.fuel_endpoint, {"source":"Natural Gas","value":500}, headers=self.header, content_type='application/json')
        status_code = response.status_code
        result = response.json()
        self.assertEqual(status_code, 201)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('type'), "fuel_combustion")
        self.assertEqual(result.get('fuel_source_type'), "ng")
        self.assertEqual(result.get('fuel_source_unit'), "thousand_cubic_feet")
        self.assertEqual(result.get('fuel_source_value'), "500.00")
    
    def test_api_create_fuel_401(self): 
        response = self.c.post(self.fuel_endpoint, {"source":"Natural Gas","value":500})
        status_code = response.status_code
        self.assertEqual(status_code, 401)
   
    def test_api_create_fuel_500(self):
        response = self.c.post(self.fuel_endpoint, {"source":"Natural Gas","value":"error"}, headers=self.header)
        status_code = response.status_code
        self.assertEqual(status_code, 500)

    def test_api_create_fuel_estimate(self):
        json_data = {"type": "fuel_combustion","fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": "500.00"}
        
        result = self.c.post(self.estimate_fuel_endpoint, json_data, headers=self.header)
        result_json = result.json()
        data = result_json.get('data')
        attributes = data.get('attributes')
        status_code = result.status_code
        self.assertEqual(status_code, 201)
        self.assertEqual(attributes.get('fuel_source_type'), "ng")
        self.assertEqual(attributes.get('fuel_source_unit'), "thousand_cubic_feet")
        self.assertEqual(attributes.get('fuel_source_value'), 500.0)

    def test_api_401_wrong_token(self):
        result = self.c.post(self.estimate_fuel_endpoint, headers={'Authorization': 'Bearer WrongToken'})
        status_code = result.status_code
        self.assertEqual(status_code, 401)

    def test_api_401_no_header(self):
        result = self.c.post(self.estimate_fuel_endpoint)
        status_code = result.status_code
        self.assertEqual(status_code, 401)

if __name__ == '__main__':
    unittest.main()