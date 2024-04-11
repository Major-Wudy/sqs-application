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