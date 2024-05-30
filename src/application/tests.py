import random
import unittest
import xmlrunner
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Create your tests here.
from application.services.domain.distance_unit_service import create_distance_unit
from application.models.distance.distance_unit import DistanceUnit

# Test DistanceUnitService and DistanceUnit
class DistanceUnitTestCase(unittest.TestCase):
    def test_distance_unit(self):
        km_du = create_distance_unit("km")
        mi_du = create_distance_unit("mi")
        self.assertEqual(km_du, "km")
        self.assertEqual(mi_du, "mi")

    def test_if_distance_unit(self):
        du = create_distance_unit("km")
        self.assertIsInstance(du, DistanceUnit)

    def test_default_distance_unit(self):
        default_du = create_distance_unit("meters")
        type_error_default_du = create_distance_unit("12")
        self.assertEqual(default_du, "km")
        self.assertEqual(type_error_default_du, "km")

from application.services.domain.electricity_service import ElectricityService
from application.models.electricity.electricity_unit import ElectricityUnit
from decimal import Decimal
# Test electricity service
class ElectricityServiceTestCase(unittest.TestCase):
    def test_create_electricity_entity(self):
        e = ElectricityService()
        elec = e.create_electricity_entity(Decimal(1678.5), "Germany", "Bavaria")
        self.assertEqual(elec.type, "electricity")
        self.assertEqual(elec.electricity_value, Decimal(1678.5))
        self.assertEqual(elec.country, "Germany")
        self.assertEqual(elec.state, "Bavaria")
        self.assertEqual(elec.electricity_unit, "kwh")

    def test_change_electricity_unit(self):
        e = ElectricityService()
        elec = e.create_electricity_entity(Decimal(1678.5), "Germany", "Bavaria")
        self.assertEqual(elec.type, "electricity")
        self.assertEqual(elec.electricity_value, Decimal(1678.5))
        self.assertEqual(elec.country, "Germany")
        self.assertEqual(elec.state, "Bavaria")
        self.assertEqual(elec.electricity_unit, "kwh")
        e.change_electricity_unit(elec, ElectricityUnit.MWH)
        self.assertEqual(elec.electricity_unit, "mwh")


from application.services.domain.flight_service import FlightService
# Test flight service
class FlightServiceTestCase(unittest.TestCase):
    def test_create_flight_entity(self):
        fs = FlightService()
        fl = fs.create_flight_entity(2, "MUC", "DUB", "KM", "economy")
        self.assertEqual(fl.type, "flight")
        self.assertEqual(fl.passengers, 2)
        self.assertEqual(fl.leg.depature_airport, "MUC")
        self.assertEqual(fl.leg.destination_airport, "DUB")
        self.assertEqual(fl.leg.cabin_class, "economy")

    def test_create_leg_object(self):
        fs = FlightService()
        leg = fs.create_leg_object("MUC", "DUB", "premium")
        self.assertEqual(leg.depature_airport, "MUC")
        self.assertEqual(leg.destination_airport, "DUB")
        self.assertEqual(leg.cabin_class, "premium")

    def test_get_cabin_class(self):
        fs = FlightService()
        cabin_economy = fs.get_cabin_class("economy")
        cabin_premium = fs.get_cabin_class("premium")
        cabin_default = fs.get_cabin_class("fist_class")
        self.assertEqual(cabin_economy, "economy")
        self.assertEqual(cabin_premium, "premium")
        self.assertEqual(cabin_default, "economy")

    def test_iata_airport_info_url(self):
        fs = FlightService()
        url = fs.iata_airport_info_url()
        self.assertEqual(url, "https://www.iata.org/en/publications/directories/code-search/?")

from application.services.domain.fuel_combustion_service import FuelService
from application.models.fuel.fuel_source_type import FuelSourceType
# Test fuel combustion service
class FuelCombustionServiceTestCase(unittest.TestCase):
    def test_create_fuel_combustion_entity(self):
        fs = FuelService()
        fuel = fs.create_fuel_combustion_entity(Decimal(120.56), "Bituminous Coal")
        self.assertEqual(fuel.type, "fuel_combustion")
        self.assertEqual(fuel.fuel_source_type, "bit")
        self.assertEqual(fuel.fuel_source_unit, "short_ton")
        self.assertEqual(fuel.consumption_value, Decimal(120.56))
        fuel_none = fs.create_fuel_combustion_entity("Kohle", Decimal(12))
        self.assertIsNone(fuel_none, None)

    def test_fuel_source_type(self):
        fst = FuelSourceType()
        natural_gas = "Natural Gas"
        waste_oil = "Waste Oil"
        atomic = "Atomic"
        waste_unit = fst.get_unit_by_name(waste_oil)
        waste = fst.get_api_name_by_name(waste_oil)
        natural_unit = fst.get_unit_by_name(natural_gas)
        natural = fst.get_api_name_by_name(natural_gas)
        fusion_unit = fst.get_unit_by_name(atomic)
        fusion = fst.get_api_name_by_name(atomic)
        self.assertEqual(waste_unit, "barrel")
        self.assertEqual(waste, "wo")
        self.assertEqual(natural_unit, "thousand_cubic_feet")
        self.assertEqual(natural, "ng")
        self.assertEqual(fusion_unit, "")
        self.assertEqual(fusion, "")

from application.services.domain.shipping_service import ShippingService
from application.services.domain.weight_unit_service import create_weight_unit
from application.services.domain.transport_service import create_transport
# Test shipping service
class ShippingServiceTestCase(unittest.TestCase):
    def test_create_shipping_entity(self):
        s = ShippingService()
        shipping = s.create_shipping_entity("kg", Decimal(2.05), "km", Decimal(250.3), "train")
        self.assertEqual(shipping.type, "shipping")
        self.assertEqual(shipping.weight_unit, "kg")
        self.assertEqual(shipping.weight_value, Decimal(2.05))
        self.assertEqual(shipping.distance_unit, "km")
        self.assertEqual(shipping.distance_value, Decimal(250.3))
        self.assertEqual(shipping.transport_method, "train")

        shipping_defaults = s.create_shipping_entity("gramm", Decimal(2.05), "kilometer", Decimal(250.3), "LKW")
        self.assertEqual(shipping_defaults.type, "shipping")
        self.assertEqual(shipping_defaults.weight_unit, "g")
        self.assertEqual(shipping_defaults.weight_value, Decimal(2.05))
        self.assertEqual(shipping_defaults.distance_unit, "km")
        self.assertEqual(shipping_defaults.distance_value, Decimal(250.3))
        self.assertEqual(shipping_defaults.transport_method, "truck")

        shipping_none = s.create_shipping_entity("gramm", "2.05", "kilometer", Decimal(250.3), "LKW")
        self.assertIsNone(shipping_none, None)

    def test_create_weight_unit(self):
        wu = create_weight_unit("lb")
        self.assertEqual(wu, "lb")
        # LB != lb sets default
        wu = create_weight_unit("LB")
        self.assertEqual(wu, "g")
        # Default
        wu = create_weight_unit("pounds")
        self.assertEqual(wu, "g")
        # TypeError sets default
        wu = create_weight_unit("12")
        self.assertEqual(wu, "g")

    def test_create_transport(self):
        method = create_transport("plane")
        self.assertEqual(method, "plane")
        method = create_transport("Zug")
        self.assertEqual(method, "truck")
        method = create_transport("12")
        self.assertEqual(method, "truck")

from application.services.infrastructure.carbon_interface_api import CarbonInterfaceRequestService
# Test Carbon Interface API
class CarbonInterfaceRequestServiceTestCase(unittest.TestCase):
    def test_auth(self):
        cirs = CarbonInterfaceRequestService()
        cirs.auth_request()


from application.services.infrastructure.estimates_service import EstimatesService
import simplejson as json
class EstimatesServiceTestCase(unittest.TestCase):
    natural_gas = "Natural Gas"
    def test_get_estimate_for_electricity_use(self):
        es = EstimatesService()
        carbon = es.get_estimate_for_electricity_use(Decimal(1650), "us", "fl", "kwm")
        carbon = json.dumps(carbon)
        self.assertTrue(carbon, dict)

        carbon = es.get_estimate_for_electricity_use("test","us", "fl", "kwm")
        self.assertIsInstance(carbon, dict)

    def test_get_estimate_for_flight(self):
        fs = EstimatesService()
        carbon = fs.get_estimate_for_flight(int(2), "MUC", "DUB", "km", "premium")
        self.assertIsInstance(carbon, dict)
    
    def test_get_estimate_for_shipping(self):
        es = EstimatesService()
        carbon = es.get_estimate_for_shipping("kg", Decimal(1.5), "km", Decimal(500), "truck")
        self.assertIsInstance(carbon, dict)
    
    def test_get_estimate_for_fuel_use(self):
        es = EstimatesService()
        carbon = es.get_estimate_for_fuel_use(Decimal(5), self.natural_gas)
        carbon = json.dumps(carbon)
        self.assertTrue(carbon, dict)
        
        carbon = es.get_estimate_for_fuel_use(Decimal(5), "", "thousand_cubic_feet", "ng")
        carbon = json.dumps(carbon)
        self.assertTrue(carbon, dict)


    def test_post(self):
        es = EstimatesService()
        response = es.post(url="")
        test_dict = {'error': 'something went wrong . Url provided?'}
        self.assertDictContainsSubset(response, test_dict)

# Automated API Tests
from django.test import Client
from dotenv import load_dotenv
import simplejson as json
import requests
class ApiTestCase(unittest.TestCase):
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
    def test_api_create_electricity(self):
        response = self.c.post(self.electricity_endpoint, {"value":123.45, "country":"us","state":"fl","unit":"kwh"}, headers={'Authorization': 'Bearer ' + self.token})
        status_code = response.status_code
        json = response.json()
        self.assertEquals(status_code, 201)
        self.assertIsInstance(json, dict)
        self.assertEquals(json.get('type'), "electricity")
        self.assertEquals(json.get('electricity_unit'), "kwh")
        self.assertEquals(json.get('electricity_value'), "123.45")
        self.assertEquals(json.get('country'), "us")
        self.assertEquals(json.get('state'), "fl")
    
    def test_api_create_electricity_401(self): 
        response = self.c.post(self.electricity_endpoint, {"value":123.45, "country":"us","state":"fl","unit":"kwh"})
        status_code = response.status_code
        self.assertEquals(status_code, 401)
    
    
    def test_api_create_electricity_estimate(self):
        json_data ={"type": "electricity", "electricity_unit": "kwh", "electricity_value": "1650", "country": "us", "state": "fl"}
        
        result = self.c.post(self.estimate_electricity_endpoint, json_data, headers={'Authorization': 'Bearer ' + self.token})
        result_json = result.json()
        data = result_json.get('data')
        attributes = data.get('attributes')
        status_code = result.status_code
        self.assertEquals(status_code, 201)
        self.assertEquals(attributes.get('country'), 'us')
        self.assertEquals(attributes.get('state'), 'fl')
        self.assertEquals(attributes.get('electricity_unit'), 'kwh')
        self.assertEquals(attributes.get('electricity_value'), 123.45)

    def test_api_create_electricity_500(self):
        response = self.c.post(self.electricity_endpoint, {"value":"test", "country":"us","state":"fl","unit":"kwh"}, headers={'Authorization': 'Bearer ' + self.token})
        status_code = response.status_code
        self.assertEquals(status_code, 500)

    # Api test flight
    def test_api_create_flight(self):
        response = self.c.post(self.flight_endpoint, {"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}, headers={'Authorization': 'Bearer ' + self.token}, content_type='application/json')
        status_code = response.status_code
        result = response.json()
        self.assertEquals(status_code, 201)
        self.assertIsInstance(result, dict)
        self.assertEquals(result.get('type'), "flight")
        self.assertEquals(result.get('passengers'), "2")
        self.assertEquals(result.get('legs')[0]["departure_airport"], "MUC")
        self.assertEquals(result.get('legs')[0]['destination_airport'], "DUB")
        self.assertEquals(result.get('legs')[0]['cabin_class'], "premium")
        self.assertEquals(result.get('distance_unit'), "km")
    
    def test_api_create_flight_401(self): 
        response = self.c.post(self.flight_endpoint, {"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"})
        status_code = response.status_code
        self.assertEquals(status_code, 401)
   
    def test_api_create_flight_500(self):
        response = self.c.post(self.flight_endpoint, {"passengers":"test","legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}, headers={'Authorization': 'Bearer ' + self.token})
        status_code = response.status_code
        self.assertEquals(status_code, 500)
    
    # Adress issue with api estimates works with normal json_data but not with simulated testclient
    """
    def test_api_create_flight_estimate(self):
        # legs not recognized as list 
        json_data = {"type": "flight","passengers": "2","legs": [{"departure_airport": "MUC","destination_airport": "DUB","cabin_class": "premium"}],"distance_unit": "km"}
        
        result = self.c.post(self.estimate_flight_endpoint, json_data, headers={'Authorization': 'Bearer ' + self.token})
        result_json = result.json()
        data = result_json.get('data')
        attributes = data.get('attributes')
        status_code = result.status_code
        self.assertEquals(status_code, 201)
        self.assertEquals(attributes.get('passengers'), 2)
        self.assertEquals(attributes.get('distance_unit'), 'km')
    """
    # Api test shipping
    def test_api_create_shipping(self):
        response = self.c.post(self.shipping_endpoint, {"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}, headers={'Authorization': 'Bearer ' + self.token}, content_type='application/json')
        status_code = response.status_code
        result = response.json()
        self.assertEquals(status_code, 201)
        self.assertIsInstance(result, dict)
        self.assertEquals(result.get('type'), "shipping")
        self.assertEquals(result.get('weight_value'), "123.45")
        self.assertEquals(result.get('weight_unit'), "g")
        self.assertEquals(result.get('distance_value'), "500.01")
        self.assertEquals(result.get('distance_unit'), "km")
        self.assertEquals(result.get('transport_method'), "plane")
    
    def test_api_create_shipping_401(self): 
        response = self.c.post(self.shipping_endpoint, {"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"})
        status_code = response.status_code
        self.assertEquals(status_code, 401)
   
    def test_api_create_shipping_500(self):
        response = self.c.post(self.shipping_endpoint, {"weight_value":"error","weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}, headers={'Authorization': 'Bearer ' + self.token})
        status_code = response.status_code
        self.assertEquals(status_code, 500)

    def test_api_create_shipping_estimate(self):
        json_data = {"type": "shipping","weight_value": "123.45","weight_unit": "g","distance_value": "500.01","distance_unit": "km","transport_method": "plane"}
        
        result = self.c.post(self.estimate_shipping_endpoint, json_data, headers={'Authorization': 'Bearer ' + self.token})
        result_json = result.json()
        data = result_json.get('data')
        attributes = data.get('attributes')
        status_code = result.status_code
        self.assertEquals(status_code, 201)
        self.assertEquals(attributes.get('weight_unit'), "g")
        self.assertEquals(attributes.get('weight_value'), 123.45)
        self.assertEquals(attributes.get('distance_value'), 500.01)
        self.assertEquals(attributes.get('distance_unit'), "km")

    # Api test fuel
    def test_api_create_fuel(self):
        response = self.c.post(self.fuel_endpoint, {"source":"Natural Gas","value":500}, headers={'Authorization': 'Bearer ' + self.token}, content_type='application/json')
        status_code = response.status_code
        result = response.json()
        self.assertEquals(status_code, 201)
        self.assertIsInstance(result, dict)
        self.assertEquals(result.get('type'), "fuel_combustion")
        self.assertEquals(result.get('fuel_source_type'), "ng")
        self.assertEquals(result.get('fuel_source_unit'), "thousand_cubic_feet")
        self.assertEquals(result.get('fuel_source_value'), "500.00")
    
    def test_api_create_fuel_401(self): 
        response = self.c.post(self.fuel_endpoint, {"source":"Natural Gas","value":500})
        status_code = response.status_code
        self.assertEquals(status_code, 401)
   
    def test_api_create_fuel_500(self):
        response = self.c.post(self.fuel_endpoint, {"source":"Natural Gas","value":"error"}, headers={'Authorization': 'Bearer ' + self.token})
        status_code = response.status_code
        self.assertEquals(status_code, 500)

    def test_api_create_fuel_estimate(self):
        json_data = {"type": "fuel_combustion","fuel_source_type": "ng","fuel_source_unit": "thousand_cubic_feet","fuel_source_value": "500.00"}
        
        result = self.c.post(self.estimate_fuel_endpoint, json_data, headers={'Authorization': 'Bearer ' + self.token})
        result_json = result.json()
        #data = result_json.get('data')
        #attributes = data.get('attributes')
        #status_code = result.status_code
        #self.assertEquals(status_code, 201)
        #self.assertEquals(attributes.get('fuel_source_type'), "ng")
        #self.assertEquals(attributes.get('fuel_source_unit'), "thousand_cubic_feet")
        #self.assertEquals(attributes.get('fuel_source_value'), 500.0)

    def test_api_401_wrong_token(self):
        result = self.c.post(self.estimate_fuel_endpoint, headers={'Authorization': 'Bearer WrongToken'})
        result_json = result.json()
        status_code = result.status_code
        self.assertEquals(status_code, 401)

    def test_api_401_no_header(self):
        result = self.c.post(self.estimate_fuel_endpoint)
        result_json = result.json()
        status_code = result.status_code
        self.assertEquals(status_code, 401)


if __name__ == '__main__':
    with open('./src/test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)