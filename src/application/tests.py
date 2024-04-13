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

from services.domain.electricity_service import create_electricity_entity
from services.domain.electricity_service import change_electricity_unit
from models.electricity.electricity_unit import ElectricityUnit
from decimal import Decimal
# Test electricity service
class ElectricityServiceTestCase(TestCase):
    def test_create_electricity_entity(self):
        elec = create_electricity_entity(Decimal(1678.5), "Germany", "Bavaria")
        self.assertEqual(elec.type, "electricity")
        self.assertEqual(elec.electricity_value, Decimal(1678.5))
        self.assertEqual(elec.country, "Germany")
        self.assertEqual(elec.state, "Bavaria")
        self.assertEqual(elec.electricity_unit, "kwh")

    def test_change_electricity_unit(self):
        elec = create_electricity_entity(Decimal(1678.5), "Germany", "Bavaria")
        self.assertEqual(elec.type, "electricity")
        self.assertEqual(elec.electricity_value, Decimal(1678.5))
        self.assertEqual(elec.country, "Germany")
        self.assertEqual(elec.state, "Bavaria")
        self.assertEqual(elec.electricity_unit, "kwh")
        change_electricity_unit(elec, ElectricityUnit.MWH)
        self.assertEqual(elec.electricity_unit, "mwh")


from services.domain.flight_service import create_flight_entity
from services.domain.flight_service import create_leg_object
from services.domain.flight_service import get_cabin_class
from services.domain.flight_service import iata_airport_info_url
# Test flight service
class FlightServiceTestCase(TestCase):
    def test_create_flight_entity(self):
        fl = create_flight_entity(2, "MUC", "DUB", "KM", "economy")
        self.assertEqual(fl.type, "flight")
        self.assertEqual(fl.passengers, 2)
        self.assertEqual(fl.leg.depature_airport, "MUC")
        self.assertEqual(fl.leg.destination_airport, "DUB")
        self.assertEqual(fl.leg.cabin_class, "economy")

    def test_create_leg_object(self):
        leg = create_leg_object("MUC", "DUB", "premium")
        self.assertEqual(leg.depature_airport, "MUC")
        self.assertEqual(leg.destination_airport, "DUB")
        self.assertEqual(leg.cabin_class, "premium")

    def test_get_cabin_class(self):
        cabin_economy = get_cabin_class("economy")
        cabin_premium = get_cabin_class("premium")
        cabin_default = get_cabin_class("fist_class")
        self.assertEqual(cabin_economy, "economy")
        self.assertEqual(cabin_premium, "premium")
        self.assertEqual(cabin_default, "economy")

    def test_iata_airport_info_url(self):
        url = iata_airport_info_url()
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

