import time
import os
#from dotenv import load_dotenv
from locust import HttpUser, task, between
from json import JSONDecodeError

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    #token = os.environ.get('TOKEN_UNIT_TEST')

    @task(2)
    def create_electricity(self):
        response = self.client.post("api/create/electricity/", json={"value":123.45, "country":"us","state":"fl","unit":"kwh"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        print("Response:", response.text)
        print("Response status code:", response.status_code)
    
    @task(2)
    def create_flight(self):
        response = self.client.post("api/create/flight/", json={"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        print("Response:", response.text)
        print("Response status code:", response.status_code)
    
    @task(2)
    def create_shipping(self):
        response = self.client.post("api/create/shipping/", json={"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        print("Response:", response.text)
        print("Response status code:", response.status_code)
    
    @task(2)
    def create_fuel(self):
        response = self.client.post("api/create/fuel/", json={"source":"Natural Gas","value":500}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        print("Response:", response.text)
        print("Response status code:", response.status_code)

    @task(1)
    def create_estimate_electricity(self):
        #elec_json = self.client.post("api/create/electricity/", json={"value":123.45, "country":"us","state":"fl","unit":"kwh"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        #response = self.client.post("api/get/estimate/electricity/", json=elec_json, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})