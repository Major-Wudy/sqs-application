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

"""Domain Service FlightService

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
"""
class FlightService():
    """create flight entity

        :author: Raphael Wudy (raphael.wudy@stud.th-rosensehim.de)
        :param passengers

    """
    @classmethod
    def create_flight_entity(cls, passengers: int, departure: str, destination: str, distance_unit: str, cabin: str) -> Flight:
        try:
            if not isinstance(passengers, int) or not isinstance(departure, str) or not isinstance(destination, str) or not isinstance(distance_unit, str) or not isinstance(cabin, str):
                raise TypeError()
            
            distance_unit = create_distance_unit(distance_unit)
            leg_object = cls.create_leg_object(departure, destination, cabin)
            return Flight(ActivityType.FLIGHT, passengers, leg_object, distance_unit)
        except TypeError:
            print("Wrong parameters flight")

    """create needed leg object for your flight entity. containing destination and departure airports and choosen cabin class

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param departure: Airport from which you are departing. International abbreviation Dublin equals DUB
    :type departure: str
    :param destination: Airport where you arrive. International abbreviation Munich equals MUC
    :type destination: str
    :param cabin: Cabin class you intending to book
    :type cabin: str
    :returns: Leg entity containing destination and departure Airports and cabin class  
    :rtype: Leg
    """
    @classmethod
    def create_leg_object(cls, departure: str, destination: str, cabin: str) -> Leg:
            cabin_class = cls.get_cabin_class(cabin)
            return Leg(departure, destination, cabin_class)

    """get cabin class from given string value

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param type: Choosen cabin class for your flight
    :type type: str
    :returns: Cabin class economy or premium
    :rtype: CabinClass
    """
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
    
    """abstract method up for implementation to get estimates from a carbon score api

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param passangers: Amount of passengers
    :type passengers: int
    :param departure:  Airport from which you are departing. International abbreviation Dublin equals DUB
    :type departure: str
    :param destination: Airport where you arrive. International abbreviation Munich equals MUC
    :type destination: str 
    :param unit: the distance unit you want your estimates be based on km or mi 
    :type unit: str
    :param cabin: Cabin class economy or premium
    :type cabin: str
    :returns: server response as json
    """
    @abstractmethod
    def get_estimate_for_flight(self, passengers: int, departure: str, destination: str, unit: str, cabin: str):
        pass
    
    """Helper function for possible ui implementation 

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :returns: IATA URL for official international airport abbreviations
    :rtype: str
    """
    @classmethod
    def iata_airport_info_url(cls) -> str:
        link = IATAAirport()
        return link.get_iata_airport_url()
    
    """converts given flight entity to json

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
    :param flight: Flight entity
    :type flight: flight
    :returns: JSON 
    :rtype: json
    """
    @classmethod
    def convert_flight_entity_to_json(cls, flight: Flight) -> json:
        return {
                "type": flight.type.value,
                "passengers": str(flight.passengers),
                "legs": [{"departure_airport":flight.leg.departure_airport, "destination_airport":flight.leg.destination_airport, "cabin_class": flight.leg.cabin_class.value}],
                "distance_unit": flight.distance_unit.value,
                }