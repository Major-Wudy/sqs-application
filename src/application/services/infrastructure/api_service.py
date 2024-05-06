import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)
src_dor = os.path.dirname(application_dir)

from rest_framework import authentication
from application.services.infrastructure.estimates_service import EstimatesService
from application.services.domain.electricity_service import ElectricityService
from application.services.domain.flight_service import FlightService
from application.services.domain.shipping_service import ShippingService
from decimal import Decimal
from rest_framework.response import Response
from rest_framework import status
import simplejson as json

class BearerAuthentication(authentication.TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:

    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''
    keyword = 'Bearer'

class ApiServices():
    @classmethod
    def create_electricity_from_post(cls, data: json) -> json:
        try:
            value = Decimal(data.get('value')).quantize(Decimal('0.01'))
            if not isinstance(value, Decimal):
                raise TypeError('value is no decimal value')

            country = data.get('country')
            if not isinstance(country, str):
                raise TypeError('country is not a string')

            state = data.get('state')
            if not isinstance(state, str):
                raise TypeError('state is not a string')

            unit = data.get('unit')
            if not isinstance(unit, str):
                raise TypeError('unit is not a string')
            es = ElectricityService()
            elec = es.create_electricity_entity(Decimal(value), country, state, unit)
            json =  es.convert_electricity_entity_to_json(elec)
            return Response(json, status=status.HTTP_201_CREATED)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except TypeError as typeErr:
            error = {"error":f"Wrong parameter type: {typeErr}"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def get_estimate_for_electricity_from_post(cls, electricity: json):
        try:
            # ToDo check json for missing values and correct syntax

            es = EstimatesService()
            json = es.get_estimate_for_electricity_use(Decimal(electricity.get("electricity_value")), electricity.get("country"), electricity.get("state"), electricity.get("electricity_unit"))
            return Response(json, status=status.HTTP_201_CREATED)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @classmethod
    def create_flight_from_post(cls, data: json) -> json:
        try:
            passengers = data.get('passengers')
            if not isinstance(passengers, int):
                raise TypeError('passengers is no int')

            unit = data.get('distance_unit')
            if not isinstance(unit, str):
                raise TypeError('unit is not a string')

            legs = data.get('legs')
            if not isinstance(legs, list):
                raise TypeError('leg is not a dict')

            fs = FlightService()
            flight = fs.create_flight_entity(passengers, legs[0]['depature'], legs[0]['destination'], unit, legs[0]['class'])
            json =  fs.convert_flight_entity_to_json(flight)
            return Response(json, status=status.HTTP_201_CREATED)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except TypeError as typeErr:
            error = {"error":f"Wrong parameter type: {typeErr}"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def create_shipping_from_post(cls, data: json) -> json:
        try:
            weight = Decimal(data.get('weight_value')).quantize(Decimal('0.01'))
            if not isinstance(weight, Decimal):
                raise TypeError('weight is no decimal value')

            weight_unit = data.get('weight_unit')
            if not isinstance(weight_unit, str):
                raise TypeError('weight_unit is not a string')

            distance = Decimal(data.get('distance_value')).quantize(Decimal('0.01'))
            if not isinstance(distance, Decimal):
                raise TypeError('distance is no decimal value')

            distance_unit = data.get('distance_unit')
            if not isinstance(distance_unit, str):
                raise TypeError('distance_unit is no string')
            
            transport = data.get('transport_method')
            if not isinstance(transport, str):
                raise TypeError('distance_unit is no string')

            ship_s = ShippingService()
            ship = ship_s.create_shipping_entity(weight_unit, weight, distance_unit, distance, transport)
            json =  ship_s.convert_shipping_entity_to_json(ship)
            return Response(json, status=status.HTTP_201_CREATED)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except TypeError as typeErr:
            error = {"error":f"Wrong parameter type: {typeErr}"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)