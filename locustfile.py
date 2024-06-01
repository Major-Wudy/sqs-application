import time
import os
#from dotenv import load_dotenv
from locust import HttpUser, task, between
from json import JSONDecodeError
import json

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    #token = os.environ.get('TOKEN_UNIT_TEST')

    @task(1)
    def create_electricity(self):
        elec = self.client.post("api/create/electricity/", json={"value":123.45, "country":"us","state":"fl","unit":"kwh"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        response = self.client.post("api/get/estimate/electricity/", json=elec.json(), headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
    
    @task(1)
    def create_flight(self):
        flight = self.client.post("api/create/flight/", json={"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        response = self.client.post("api/get/estimate/flight/", json=flight.json(), headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
    
    @task(1)
    def create_shipping(self):
        shipping = self.client.post("api/create/shipping/", json={"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        response = self.client.post("api/get/estimate/shipping/", json=shipping.json(), headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
    
    @task(1)
    def create_fuel(self):
        fuel = self.client.post("api/create/fuel/", json={"source":"Natural Gas","value":500}, headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})
        response = self.client.post("api/get/estimate/fuel/", json=fuel.json(), headers={'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"})