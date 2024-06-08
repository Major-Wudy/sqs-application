import time
import os
from locust import HttpUser, task, between
import json

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    header = {'Authorization': 'Bearer ae7c53dcaafe8887d331003252fa90f6c5ff5059', "Content-Type": "application/json"}

    def create_electricity(self):
        elec = self.client.post("api/create/electricity/", json={"value":123.45, "country":"us","state":"fl","unit":"kwh"}, headers=self.header)
        response = self.client.post("api/get/estimate/electricity/", json=elec.json(), headers=self.header)
        print(response.text)
    
    def create_flight(self):
        flight = self.client.post("api/create/flight/", json={"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}, headers=self.header)
        response = self.client.post("api/get/estimate/flight/", json=flight.json(), headers=self.header)
        print(response.text)
    
    def create_shipping(self):
        shipping = self.client.post("api/create/shipping/", json={"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}, headers=self.header)
        response = self.client.post("api/get/estimate/shipping/", json=shipping.json(), headers=self.header)
        print(response.text)
    
    def create_fuel(self):
        fuel = self.client.post("api/create/fuel/", json={"source":"Natural Gas","value":500}, headers=self.header)
        response = self.client.post("api/get/estimate/fuel/", json=fuel.json(), headers=self.header)
        print(response.text)