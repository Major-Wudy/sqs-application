from django.test import TestCase
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Create your tests here.
from services.domain.distance_unit_service import create_distance_unit
from models.distance.distance_unit import DistanceUnit
from decimal import Decimal

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