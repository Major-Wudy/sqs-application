import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(application_dir)

from application.models.activity.activity_type import ActivityType
from application.models.flight.flight import Flight
from application.models.flight.leg import Leg
from application.models.flight.iata_airport import IATAAirport
from application.models.flight.cabin_class import CabinClass
from application.services.domain.distance_unit_service import create_distance_unit
from abc import ABC, abstractmethod
import simplejson as json

class FlightService():
    @classmethod
    def create_flight_entity(cls, passengers: int, depature: str, destination: str, distance_unit: str, cabin: str) -> Flight:
        try:
            if not isinstance(passengers, int) or not isinstance(depature, str) or not isinstance(destination, str) or not isinstance(distance_unit, str) or not isinstance(cabin, str):
                raise TypeError()
            
            distance_unit = create_distance_unit(distance_unit)
            leg_object = cls.create_leg_object(depature, destination, cabin)
            return Flight(ActivityType.FLIGHT, passengers, leg_object, distance_unit)
        except TypeError:
            print("Wrong parameters flight")

    @classmethod
    def create_leg_object(cls, depature: str, destination: str, cabin: str) -> Leg:
            cabin_class = cls.get_cabin_class(cabin)
            return Leg(depature, destination, cabin_class)

    @classmethod
    def get_cabin_class(cls, type: str) -> CabinClass:
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
    def get_estimate_for_flight(self, passengers: int, depature: str, destination: str, unit: str, cabin: str):
        """
        Args:
            api_interface (CarbonInterfaceRequestService): Das API Interface, welches den direkten HTTP-Call an die externe API sendet

        Returns:
            dict: Die Antwortdaten als Python-Datenstruktur (z. B. ein JSON-Objekt).
        """
        pass
    
    @classmethod
    def iata_airport_info_url(cls) -> str:
        link = IATAAirport()
        return link.get_iata_airport_url()

    @classmethod
    def convert_flight_entity_to_json(cls, flight: Flight) -> json:
        return {
                "type": flight.type.value,
                "passengers": str(flight.passengers),
                "legs": [{"departure_airport":flight.leg.depature_airport, "destination_airport":flight.leg.destination_airport, "cabin_class": flight.leg.cabin_class.value}],
                "distance_unit": flight.distance_unit.value,
                }