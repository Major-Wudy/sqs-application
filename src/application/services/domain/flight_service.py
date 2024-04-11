import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from models.activity.activity_type import ActivityType
from models.flight.flight import Flight
from models.flight.leg import Leg
from models.flight.iata_airport import IATAAirport
from models.flight.cabin_class import CabinClass
from services.domain.distance_unit_service import create_distance_unit

def create_flight(type: ActivityType, passengers: int, depature: str, destination: str, distance_unit: str, cabin: str) -> Flight:
    try:
        if not isinstance(type, ActivityType) or not isinstance(passengers, int) or not isinstance(depature, str) or not isinstance(destination, str) or not isinstance(distance_unit, str) or not isinstance(cabin: str):
            raise TypeError()
        
        distance_unit = create_distance_unit(distance_unit)
        legObject = create_leg_object(depature, destination, cabin)
        return Flight(ActivityType.FLIGHT, passengers, legObject, distanceUnit)

def create_leg_object(depature: str, destination: str, cabin: str) -> Leg:
        cabin_class = get_cabin_class(cabin)
        return Leg(depature, destination, cabin_class)

def get_cabin_class(type: str) -> CabinClass:
    try: 
        if not isinstance(type: str):
            raise TypeError()

        if unit == "economy":
            return CabinClass.ECONOMY
        elif unit == "premium":
            return CabinClass.PREMIUM
        else:
            # Set Km as default value
            return CabinClass.ECONOMY
    except TypeError:
        return CabinClass.ECONOMY

def get_estimate_for_flight():

def iata_airport_info_url() -> str:
    link = IATAAirport()
    return link.get_iata_airport_url()