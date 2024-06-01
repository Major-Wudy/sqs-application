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

from application.services.domain.carbon_service import CarbonService
from application.models.carbon.score import Score
# Test CarbonService
class CarbonServiceTestCase(unittest.TestCase):
    def test_create_carbon_score(self):
        cs = CarbonService()
        score = cs.create_carbon_score(Decimal(123.45), Decimal(56.54), Decimal(10.12), Decimal(100), "custom_session_id")
        wrong_params = cs.create_carbon_score("123", "321","wada", "wasd", Decimal(123))
        self.assertIsInstance(score, Score)
        self.assertIsInstance(wrong_params, Score)
        self.assertEqual(score.score_g.quantize(Decimal('0.01')), Decimal(123.45).quantize(Decimal('0.01')))
        self.assertEqual(score.score_kg.quantize(Decimal('0.01')), Decimal(56.54).quantize(Decimal('0.01')))
        self.assertEqual(score.score_lb.quantize(Decimal('0.01')), Decimal(10.12).quantize(Decimal('0.01')))
        self.assertEqual(score.score_mt.quantize(Decimal('0.01')), Decimal(100).quantize(Decimal('0.01')))
        self.assertEqual(score.session_id, "custom_session_id")
        self.assertEqual(wrong_params.score_g, Decimal(0))
        self.assertEqual(wrong_params.score_kg, Decimal(0))
        self.assertEqual(wrong_params.score_lb, Decimal(0))
        self.assertEqual(wrong_params.score_mt, Decimal(0))
        self.assertEqual(wrong_params.session_id, "")

    def test_convert_score_to_json(self):
        cs = CarbonService()
        score = cs.create_carbon_score(Decimal(432.13), Decimal(56), Decimal(11.11), Decimal(90), "json_session_id")
        score_json = cs.convert_score_to_json(score)
        self.assertIsInstance(score_json, dict)
        self.assertEqual(score_json.get('carbon_g'), "432.13")
        self.assertEqual(score_json.get('carbon_kg'), "56.00")
        self.assertEqual(score_json.get('carbon_lb'), "11.11")
        self.assertEqual(score_json.get('carbon_mt'), "90.00")
        self.assertEqual(score_json.get('sessionId'), "json_session_id")

        nothing_json = cs.convert_score_to_json("no score")
        self.assertIsInstance(nothing_json, dict)
        self.assertEqual(nothing_json.get('carbon_g'), "0")
        self.assertEqual(nothing_json.get('carbon_kg'), "0")
        self.assertEqual(nothing_json.get('carbon_lb'), "0")
        self.assertEqual(nothing_json.get('carbon_mt'), "0")
        self.assertEqual(nothing_json.get('sessionId'), "")


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

from application.services.infrastructure.api_service import ApiServices
class ApiServiceTestCase(unittest.TestCase):
    api = ApiServices()
    def test_create_electricity_from_post(self):
        elec_json  = {"value":100.5,"country":"us","state":"fl","unit":"kwh"}
        resp = self.api.create_electricity_from_post(elec_json)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp, dict)

        wrong_elec  = {"test":100.5,"country":"us","state":"fl","unit":"kwh"}
        resp = self.api.create_electricity_from_post(wrong_elec)
        self.assertEqual(resp.status_code, 400)
        self.assertTrue(resp, dict)
        
        wrong_elec  = {"value":"wasd","country":"us","state":"fl","unit":"kwh"}
        resp = self.api.create_electricity_from_post(wrong_elec)
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

    def test_get_estimate_for_electricity_from_post(self):
        resp = self.api.get_estimate_for_electricity_from_post("test")
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

    def test_create_flight_from_post(self):
        flight_json = {"passengers":2,"legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}
        resp = self.api.create_flight_from_post(flight_json)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp, dict)

        wrong_json = {"passengers":2,"legs":"test","distance_unit":"km"}
        resp = self.api.create_flight_from_post(wrong_json)
        self.assertEqual(resp.status_code, 400)
        self.assertTrue(resp, dict)
        
        wrong_json = {"passengers":"test","legs":[{"depature":"MUC","destination":"DUB","class":"premium"}],"distance_unit":"km"}
        resp = self.api.create_flight_from_post(wrong_json)
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

    def test_get_estimate_for_flight_from_post(self):
        resp = self.api.get_estimate_for_flight_from_post("test")
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

    def test_create_shipping_from_post(self):
        shipping_json = {"weight_value":123.45,"weight_unit": "g","distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}
        resp = self.api.create_shipping_from_post(shipping_json)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp, dict)

        wrong_json = {"weight_value":123.45,"weight_unit": 2,"distance_value": 500.01,"distance_unit": "km","transport_method": "plane"}
        resp = self.api.create_shipping_from_post(wrong_json)
        self.assertEqual(resp.status_code, 400)
        self.assertTrue(resp, dict)
        
        wrong_json = "test"
        resp = self.api.create_shipping_from_post(wrong_json)
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

    def test_get_estimate_for_shipping_from_post(self):
        resp = self.api.get_estimate_for_shipping_from_post("test")
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

    def test_create_fuel_from_post(self):
        fuel_json = {"source":"Natural Gas","value":500}
        resp = self.api.create_fuel_from_post(fuel_json)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp, dict)

        wrong_json = {"source":500,"value":500}
        resp = self.api.create_fuel_from_post(wrong_json)
        self.assertEqual(resp.status_code, 400)
        self.assertTrue(resp, dict)
        
        wrong_json = {"source":"Natural Gas","value":"wasd"}
        resp = self.api.create_fuel_from_post(wrong_json)
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

    def test_get_estimate_for_fuel_from_post(self):
        resp = self.api.get_estimate_for_fuel_from_post("test")
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(resp, dict)

from django.test import Client
from dotenv import load_dotenv
import simplejson as json
import requests
class ApiTestCase(unittest.TestCase):
    c = Client()
    electricity_endpoint = "/api/create/electricity/"
    flight_endpoint = "/api/create/flight/"
    shipping_endpoint = "/api/create/shipping/"
    fuel_endpoint = "/api/create/fuel/"
    header = {'Authorization': 'Bearer ' + os.environ.get('TOKEN_UNIT_TEST')}
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

        response = self.c.post(self.electricity_endpoint, {"test"}, headers=self.header)
        status_code = response.status_code
        self.assertEqual(status_code, 500)

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

        response = self.c.post(self.flight_endpoint, {"test"}, headers=self.header)
        status_code = response.status_code
        self.assertEqual(status_code, 500)

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

        response = self.c.post(self.shipping_endpoint, {"test"}, headers=self.header)
        status_code = response.status_code
        self.assertEqual(status_code, 500)

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

        response = self.c.post(self.fuel_endpoint, {"test"}, headers=self.header)
        status_code = response.status_code
        self.assertEqual(status_code, 500)

if __name__ == '__main__':
    with open('./src/test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)