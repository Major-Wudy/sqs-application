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
from abc import ABC, abstractmethod
import simplejson as json

class FlightService():
    @classmethod
    def create_flight_entity(self, passengers: int, depature: str, destination: str, distance_unit: str, cabin: str) -> Flight:
        try:
            if not isinstance(passengers, int) or not isinstance(depature, str) or not isinstance(destination, str) or not isinstance(distance_unit, str) or not isinstance(cabin, str):
                raise TypeError()
            
            distance_unit = create_distance_unit(distance_unit)
            legObject = self.create_leg_object(depature, destination, cabin)
            return Flight(ActivityType.FLIGHT, passengers, legObject, distance_unit)
        except TypeError:
            print("Wrong parameters flight")

    @classmethod
    def create_leg_object(self, depature: str, destination: str, cabin: str) -> Leg:
            cabin_class = self.get_cabin_class(cabin)
            return Leg(depature, destination, cabin_class)

    @classmethod
    def get_cabin_class(self, type: str) -> CabinClass:
        try: 
            if not isinstance(type, str):
                raise TypeError()

            if type == "economy":
                return CabinClass.ECONOMY
            elif type == "premium":
                return CabinClass.PREMIUM
            else:
                # Set Km as default value
                return CabinClass.ECONOMY
        except TypeError:
            return CabinClass.ECONOMY
    
    @abstractmethod
    def get_estimate_for_flight(self, data: dict):
        """
        Args:
            api_interface (CarbonInterfaceRequestService): Das API Interface, welches den direkten HTTP-Call an die externe API sendet

        Returns:
            dict: Die Antwortdaten als Python-Datenstruktur (z. B. ein JSON-Objekt).
        """
        pass
    
    @classmethod
    def iata_airport_info_url(self) -> str:
        link = IATAAirport()
        return link.get_iata_airport_url()

    @classmethod
    def convert_flight_entity_to_json(self, flight: Flight) -> json:
        return json.dumps({
                "type": flight.type,
                "passengers": flight.passengers,
                "legs": [{"departure_airport":flight.leg.depature_airport, "destination_airport":flight.leg.destination_airport, "cabin_class": flight.leg.cabin_class}],
                "distance_unit": flight.distance_unit,
                })