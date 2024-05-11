import pytest
import requests

from wiremock.testing.testcontainer import wiremock_container
from wiremock.constants import Config
from wiremock.client import *

@pytest.fixture # (1)
def wiremock_server():
    
    mappings = [
        (
            "electricity.json", 
            {
                "request": {
                    "method": "POST",
                    "url": "/api/v1/estimates",
                    "headers":{
                        "Authorization":{
                            "matches":"Bearer API_KEY"
                        }
                    },
                    "bodyPatterns": [
                        {
                            "equalToJson":{"type": "electricity","electricity_unit": "${json-unit.regex}^[a-z]{3}$","electricity_value": "${json-unit.any-number}","country": "${json-unit.regex}^[a-z]{2}$"}
                        }
                    ]
                },
                "response": {
                    "status": 201,
                    "body":'{"data": {"id": "ef065a14-651f-4323-a64a-83890348af22","type": "estimate","attributes": {"country": "us","state": "fl","electricity_unit": "kwh","electricity_value": 123.45,"estimated_at": "2024-05-09T17:25:52.041Z","carbon_g": 48937,"carbon_lb": 107.89,"carbon_kg": 48.94,"carbon_mt": 0.05}}}',
                    "headers": {
                        "Content-Type": "application/json"
                    }
                }
            },
        ),
        (
            "flught.json",
            {
                "request": {
                    "method": "POST",
                    "url": "/api/v1/estimates",
                    "headers":{
                        "Authorization":{
                            "matches":"Bearer API_KEY"
                        }
                    },
                    "bodyPatterns": [
                        {
                            "equalToJson":{"type": "flight","passengers": "${json-unit.any-number}","legs": [{"departure_airport": "${json-unit.regex}^[A-Z]{3}$", "destination_airport": "${json-unit.regex}^[A-Z]{3}$", "cabin_class":"${json-unit.regex}^premium$|^economy$"}]}                    }
                    ]
                },
                "response": {
                    "status": 201,
                    "body": '{"data": {"id": "42999c38-a2b7-48e5-9ec0-bc60a7d870c1","type": "estimate","attributes": {"passengers": 2,"legs": [{"departure_airport": "MUC","destination_airport": "DUB","cabin_class": "premium"}],"distance_value": 1481.06,"distance_unit": "km","estimated_at": "2024-05-09T17:29:36.986Z","carbon_g": 391356,"carbon_lb": 862.79,"carbon_kg": 391.36,"carbon_mt": 0.39}}}',
                    "headers": {
                        "Content-Type": "application/json"
                    }
                }
            },
        ),
        (
            "shipping.json",
            {
                "request": {
                    "method": "POST",
                    "url": "/api/v1/estimates",
                    "headers":{
                        "Authorization":{
                            "matches":"Bearer API_KEY"
                        }
                    },
                    "bodyPatterns": [
                        {
                            "equalToJson":{"type": "shipping","weight_value": "${json-unit.any-number}","weight_unit": "${json-unit.regex}^[a-z]{1,2}$","distance_value": "${json-unit.any-number}","distance_unit": "${json-unit.regex}^[a-z]{2}$","transport_method": "${json-unit.regex}^truck$|^plane$|^train$|^ship$"}
                        }
                    ]
                },
                "response": {
                    "status": 201,
                    "body": '{"data": {"id": "b4ac6ce9-ba1b-4ee4-b30e-b73e16465bfd","type": "estimate","attributes": {"distance_value": 500.01,"weight_unit": "g","transport_method": "plane","weight_value": 123.45,"distance_unit": "km","estimated_at": "2024-05-09T17:18:01.418Z","carbon_g": 37,"carbon_lb": 0.08,"carbon_kg": 0.04,"carbon_mt": 0.0}}}',
                    "headers": {
                        "Content-Type": "application/json"
                    }
                }
            },
        ),
        (
            "shipping401.json",
            {
                "request": {
                    "method": "POST",
                    "url": "/api/v1/estimates",
                    "headers":{
                        "Authorization":{
                            "absent":"true"
                        }
                    }
                },
                "response": {
                    "status": 401,
                    "body": '{"error":"Unauthorized"}',
                    "headers": {
                        "Content-Type": "application/json"
                    }
                }
            },
        ),
        (
            "shipping401_2.json",
            {
                "request": {
                    "method": "POST",
                    "url": "/api/v1/estimates",
                    "headers":{
                        "Authorization":{
                            "doesNotMatch":"Bearer API_KEY"
                        }
                    }
                },
                "response": {
                    "status": 401,
                    "body": '{"error":"Unauthorized"}',
                    "headers": {
                        "Content-Type": "application/json"
                    }
                }
            },
        ),
        (
            "fuel.json",
            {
                "request": {
                    "method": "POST",
                    "url": "/api/v1/estimates",
                    "headers":{
                        "Authorization":{
                            "matches":"Bearer API_KEY"
                        }
                    },
                    "bodyPatterns": [
                        {
                            "equalToJson":{"type": "fuel_combustion","fuel_source_type": "${json-unit.regex}^[a-z]{2,3}$","fuel_source_unit": "${json-unit.any-string}","fuel_source_value": "${json-unit.any-number}"}
                        }
                    ]
                },
                "response": {
                    "status": 201,
                    "body": '{"data": {"id": "97e1b97b-9c3b-4e87-b2f4-4c20131d162d","type": "estimate","attributes": {"fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": 500.0,"estimated_at": "2024-05-09T17:34:39.806Z","carbon_g": 26560000,"carbon_lb": 58554.78,"carbon_kg": 26560.0,"carbon_mt": 26.56}}}',
                    "headers": {
                        "Content-Type": "application/json"
                    }
                }
            }
        )
    ]

    with wiremock_container(mappings=mappings, secure=False) as wm:
        Config.base_url = wm.get_url("__admin") # (2)     
        yield wm

def test_post_estimates_electricity(wiremock_server): # (4)
    electricity = {"type": "electricity","electricity_unit": "kwh","electricity_value":123,"country": "us"}
    response = requests.post(wiremock_server.get_url("/api/v1/estimates"), headers={'Authorization':'Bearer API_KEY', 'Content-Type':'application/json'}, json=electricity)
    assert response.status_code == 201
    assert response.json() == {"data": {"id": "ef065a14-651f-4323-a64a-83890348af22","type": "estimate","attributes": {"country": "us","state": "fl","electricity_unit": "kwh","electricity_value": 123.45,"estimated_at": "2024-05-09T17:25:52.041Z","carbon_g": 48937,"carbon_lb": 107.89,"carbon_kg": 48.94,"carbon_mt": 0.05}}}

def test_post_estimates_flight(wiremock_server): # (4)
    flight = {"type": "flight","passengers":3,"legs": [{"departure_airport": "MUC", "destination_airport": "DUB", "cabin_class":"premium"}]}
    response = requests.post(wiremock_server.get_url("/api/v1/estimates"), headers={'Authorization':'Bearer API_KEY', 'Content-Type':'application/json'}, json=flight)
    assert response.status_code == 201
    assert response.json() == {"data": {"id": "42999c38-a2b7-48e5-9ec0-bc60a7d870c1","type": "estimate","attributes": {"passengers": 2,"legs": [{"departure_airport": "MUC","destination_airport": "DUB","cabin_class": "premium"}],"distance_value": 1481.06,"distance_unit": "km","estimated_at": "2024-05-09T17:29:36.986Z","carbon_g": 391356,"carbon_lb": 862.79,"carbon_kg": 391.36,"carbon_mt": 0.39}}}

def test_post_estimates_fuel(wiremock_server): # (4)
    fuel = {"type": "fuel_combustion","fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": 130}
    response = requests.post(wiremock_server.get_url("/api/v1/estimates"), headers={'Authorization':'Bearer API_KEY', 'Content-Type':'application/json'}, json=fuel)
    assert response.status_code == 201
    assert response.json() == {"data": {"id": "97e1b97b-9c3b-4e87-b2f4-4c20131d162d","type": "estimate","attributes": {"fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": 500.0,"estimated_at": "2024-05-09T17:34:39.806Z","carbon_g": 26560000,"carbon_lb": 58554.78,"carbon_kg": 26560.0,"carbon_mt": 26.56}}}

def test_post_estimates_shipping(wiremock_server): # (4)
    shipping = {"type": "shipping","weight_value": 1.5,"weight_unit": "kg","distance_value": 800,"distance_unit": "km","transport_method": "truck"}
    response = requests.post(wiremock_server.get_url("/api/v1/estimates"), headers={'Authorization':'Bearer API_KEY', 'Content-Type':'application/json'}, json=shipping)
    assert response.status_code == 201
    assert response.json() == {"data": {"id": "b4ac6ce9-ba1b-4ee4-b30e-b73e16465bfd","type": "estimate","attributes": {"distance_value": 500.01,"weight_unit": "g","transport_method": "plane","weight_value": 123.45,"distance_unit": "km","estimated_at": "2024-05-09T17:18:01.418Z","carbon_g": 37,"carbon_lb": 0.08,"carbon_kg": 0.04,"carbon_mt": 0.0}}}

def test_post_estimates_shipping_404(wiremock_server): # (4)
    shipping = {"type": "shipping","weight_value": 1.5,"weight_unit": "kg","distance_value": 800,"distance_unit": "km","transport_method": "truck"}
    response = requests.post(wiremock_server.get_url("/api/estimates"), headers={'Authorization':'Bearer API_KEY', 'Content-Type':'application/json'}, json=shipping)
    assert response.status_code == 404

def test_post_estimates_shipping_401(wiremock_server): # (4)
    shipping = {"type": "shipping","weight_value": 1.5,"weight_unit": "kg","distance_value": 800,"distance_unit": "km","transport_method": "truck"}
    response = requests.post(wiremock_server.get_url("/api/v1/estimates"), headers={'Authorization':'Bearer WRONG_KEY', 'Content-Type':'application/json'}, json=shipping)
    assert response.status_code == 401

def test_post_estimates_shipping_401_no_auth(wiremock_server): # (4)
    shipping = {"type": "shipping","weight_value": 1.5,"weight_unit": "kg","distance_value": 800,"distance_unit": "km","transport_method": "truck"}
    response = requests.post(wiremock_server.get_url("/api/v1/estimates"), headers={'Content-Type':'application/json'}, json=shipping)
    assert response.status_code == 401