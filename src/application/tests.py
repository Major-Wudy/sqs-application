from django.test import TestCase
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Create your tests here.
from services.domain.distance_unit_service import create_distance_unit
from models.distance.distance_unit import DistanceUnit

# Test DistanceUnitService and DistanceUnit
class DistanceUnitTestCase(TestCase):
    def test_distance_unit(self):
        km_du = create_distance_unit("km")
        mi_du = create_distance_unit("mi")
        self.assertEqual(km_du, "km")
        self.assertEqual(mi_du, "mi")

    def test_if_distance_unit(self):
        du = create_distance_unit("km")
        self.assertTrue(isinstance(du, DistanceUnit))

    def test_default_distance_unit(self):
        default_du = create_distance_unit("meters")
        type_error_default_du = create_distance_unit(1)
        self.assertEqual(default_du, "km")
        self.assertEqual(type_error_default_du, "km")

#from services.domain.electricity_service import ElectricityService
import application.services.domain.electricity_service as es
from models.electricity.electricity_unit import ElectricityUnit
from decimal import Decimal
# Test electricity service
class ElectricityServiceTestCase(TestCase):
    def test_create_electricity_entity(self):
        e = es.ElectricityService()
        elec = e.create_electricity_entity(Decimal(1678.5), "Germany", "Bavaria")
        self.assertEqual(elec.type, "electricity")
        self.assertEqual(elec.electricity_value, Decimal(1678.5))
        self.assertEqual(elec.country, "Germany")
        self.assertEqual(elec.state, "Bavaria")
        self.assertEqual(elec.electricity_unit, "kwh")

    def test_change_electricity_unit(self):
        e = es.ElectricityService()
        elec = e.create_electricity_entity(Decimal(1678.5), "Germany", "Bavaria")
        self.assertEqual(elec.type, "electricity")
        self.assertEqual(elec.electricity_value, Decimal(1678.5))
        self.assertEqual(elec.country, "Germany")
        self.assertEqual(elec.state, "Bavaria")
        self.assertEqual(elec.electricity_unit, "kwh")
        e.change_electricity_unit(elec, ElectricityUnit.MWH)
        self.assertEqual(elec.electricity_unit, "mwh")


from services.domain.flight_service import FlightService
# Test flight service
class FlightServiceTestCase(TestCase):
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

from services.domain.fuel_combustion_service import create_fuel_combustion_entity
from models.fuel.fuel_source_type import FuelSourceType
# Test fuel combustion service
class FuelCombustionServiceTestCase(TestCase):
    def test_create_fuel_combustion_entity(self):
        fuel = create_fuel_combustion_entity("Bituminous Coal", Decimal(120.56))
        self.assertEqual(fuel.type, "fuel_combustion")
        self.assertEqual(fuel.fuel_source_type, "bit")
        self.assertEqual(fuel.fuel_source_unit, "short_ton")
        self.assertEqual(fuel.consumption_value, Decimal(120.56))
        fuel_none = create_fuel_combustion_entity("Kohle", 12)
        self.assertEqual(fuel_none, None)

    def test_fuel_source_type(self):
        fst = FuelSourceType()
        waste_unit = fst.get_unit_by_name("Waste Oil")
        waste = fst.get_api_name_by_name("Waste Oil")
        natural_unit = fst.get_unit_by_name("Natural Gas")
        natural = fst.get_api_name_by_name("Natural Gas")
        fusion_unit = fst.get_unit_by_name("Atomic")
        fusion = fst.get_api_name_by_name("Atomic")
        self.assertEqual(waste_unit, "barrel")
        self.assertEqual(waste, "wo")
        self.assertEqual(natural_unit, "thousand_cubic_feet")
        self.assertEqual(natural, "ng")
        self.assertEqual(fusion_unit, "")
        self.assertEqual(fusion, "")

from services.domain.shipping_service import ShippingService
from services.domain.weight_unit_service import create_weight_unit
from services.domain.transport_service import create_transport
# Test shipping service
class ShippingServiceTestCase(TestCase):
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
        self.assertEqual(shipping_none, None)

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
        wu = create_weight_unit(1)
        self.assertEqual(wu, "g")

    def test_create_transport(self):
        method = create_transport("plane")
        self.assertEqual(method, "plane")
        method = create_transport("Zug")
        self.assertEqual(method, "truck")
        method = create_transport(1)
        self.assertEqual(method, "truck")

from services.infrastructure.carbon_interface_api import CarbonInterfaceRequestService
# Test Carbon Interface API
class CarbonInterfaceRequestServiceTestCase(TestCase):
    def test_auth(self):
        cirs = CarbonInterfaceRequestService()
        cirs.auth_request()


from services.infrastructure.estimates_service import EstimatesService
import simplejson as json
class EstimatesServiceTestCase(TestCase):
    def test_get_estimate_for_electricity_use(self):
        es = EstimatesService()
        data = {"type" : "electricity", "unit" : "kwh", "value" : Decimal(1650), "country": "us", "state": "fl"}
        carbon = es.get_estimate_for_electricity_use(data)
        carbon = json.dumps(carbon)
        self.assertTrue(carbon, dict)

    def test_get_estimate_for_flight(self):
        fs = EstimatesService()
        data = {"passengers": int(2), "depature" : "MUC", "destination": "DUB", "unit" : "km", "class":"premium"}
        carbon = fs.get_estimate_for_flight(data)
        carbon = json.dumps(carbon)
        self.assertTrue(carbon, dict) 
    
    def test_get_estimate_for_shipping(self):
        es = EstimatesService()
        data = {"weight_unit": "kg", "weight_value" : Decimal(500), "distance_unit": "km", "distance_value" : Decimal(254), "transport_method":"truck"}
        carbon = es.get_estimate_for_shipping(data)
        carbon = json.dumps(carbon)
        self.assertTrue(carbon, dict)