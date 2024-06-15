import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)
src_dor = os.path.dirname(application_dir)

from rest_framework import authentication
from application.services.infrastructure.estimates_service import EstimatesService
from application.services.domain_interface.domain_service_interface import DomainServiceInterface
from application.services.infrastructure_interface.database_interface import DatabaseServiceInterface
from decimal import Decimal
from rest_framework.response import Response
from rest_framework import status
import simplejson as json

"""Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:

    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
"""
class BearerAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'

"""Infrastructure Service ApiSerivces

    :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
"""
class ApiServices():
    content_json = "application/json"

    """create electricity entitiy from post request with domain service electricity services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param data: request data as json
        :type data: json
        :returns: server response as json
        :rtype: json
    """
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
            ds = DomainServiceInterface()
            elec = ds.create_electricity_entity(Decimal(value), country, state, unit)
            json_data =  ds.convert_electricity_entity_to_json(elec)
            return Response(json_data, status=status.HTTP_201_CREATED, content_type=cls.content_json)
        except TypeError as typeErr:
            error = {"error":f"Wrong parameter type: {typeErr}"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST, content_type=cls.content_json)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """estimates carbon score for electricity entitiy from post request with domain service electricity services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param electricity: electricity entity as json
        :type electricity: json
        :returns: server response as json
        :rtype: json
    """
    @classmethod
    def get_estimate_for_electricity_from_post(cls, electricity: json) -> json:
        try:
            es = EstimatesService()
            json = es.get_estimate_for_electricity_use(Decimal(electricity.get("electricity_value")), electricity.get("country"), electricity.get("state"), electricity.get("electricity_unit"))
            return Response(json, status=status.HTTP_201_CREATED, content_type=cls.content_json)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """create flight entitiy from post request with domain service flight services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param data: request data as json
        :type data: json
        :returns: server response as json
        :rtype: json
    """ 
    @classmethod
    def create_flight_from_post(cls, data: json) -> json:
        try:
            passengers = data.get('passengers')
            unit = data.get('distance_unit')
            if not isinstance(unit, str):
                raise TypeError('unit is not a string')

            legs = data.get('legs')
            if not isinstance(legs, list):
                raise TypeError('leg is not a dict')

            ds = DomainServiceInterface()
            flight = ds.create_flight_entity(int(passengers), legs[0]['departure'], legs[0]['destination'], unit, legs[0]['class'])
            json =  ds.convert_flight_entity_to_json(flight)
            return Response(json, status=status.HTTP_201_CREATED, content_type=cls.content_json)
        except TypeError as typeErr:
            error = {"error":f"Wrong parameter type: {typeErr}"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST, content_type=cls.content_json)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """estimates carbon score for flight entitiy from post request with domain service flight services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param flight: flight entity as json
        :type flight: json
        :returns: server response as json
        :rtype: json
    """
    @classmethod
    def get_estimate_for_flight_from_post(cls, flight: json) -> json:
        try:
            legs = flight.get('legs')
            if not isinstance(legs, list):
                raise TypeError('legs is not a list')

            es = EstimatesService()
            json_data = es.get_estimate_for_flight(flight.get("passengers"), legs[0]['departure_airport'], legs[0]['destination_airport'], flight.get("distance_unit"), legs[0]['cabin_class'])
            return Response(json_data, status=status.HTTP_201_CREATED, content_type=cls.content_json)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """create shipping entitiy from post request with domain service shipping services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param data: request data as json
        :type data: json
        :returns: server response as json
        :rtype: json
    """
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

            ds = DomainServiceInterface()
            ship = ds.create_shipping_entity(weight_unit, weight, distance_unit, distance, transport)
            json =  ds.convert_shipping_entity_to_json(ship)
            return Response(json, status=status.HTTP_201_CREATED, content_type=cls.content_json)
        except TypeError as typeErr:
            error = {"error":f"Wrong parameter type: {typeErr}"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST, content_type=cls.content_json)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """estimates carbon score for shipping entitiy from post request with domain service shipping services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param shipping: shipping entity as json
        :type shipping: json
        :returns: server response as json
        :rtype: json
    """
    @classmethod
    def get_estimate_for_shipping_from_post(cls, shipping: json) -> json:
        try:
            es = EstimatesService()
            json = es.get_estimate_for_shipping(shipping.get("weight_unit"), Decimal(shipping.get("weight_value")), shipping.get("distance_unit"), Decimal(shipping.get("distance_value")), shipping.get("transport_method"))
            return Response(json, status=status.HTTP_201_CREATED)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """create fuel entitiy from post request with domain service fuel services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param data: request data as json
        :type data: json
        :returns: server response as json
        :rtype: json
    """
    @classmethod
    def create_fuel_from_post(cls, data: json) -> json:
        try:
            source = data.get('source')
            if not isinstance(source, str):
                raise TypeError('source is not a string')

            consumption = Decimal(data.get('value')).quantize(Decimal('0.01'))
            if not isinstance(consumption, Decimal):
                raise TypeError('consumption is no decimal value')

            ds = DomainServiceInterface()
            fuel = ds.create_fuel_combustion_entity(consumption, source)
            json =  ds.convert_fuel_entity_to_json(fuel)
            return Response(json, status=status.HTTP_201_CREATED)
        except TypeError as typeErr:
            error = {"error":f"Wrong parameter type: {typeErr}"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST, content_type=cls.content_json)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """estimates carbon score for fuel entitiy from post request with domain service fuel services

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param fuel: fuel entity as json
        :type fuel: json
        :returns: server response as json
        :rtype: json
    """
    @classmethod
    def get_estimate_for_fuel_from_post(cls, fuel: json) -> json:
        try:
            es = EstimatesService()
            json = es.get_estimate_for_fuel_use(Decimal(fuel.get("fuel_source_value")), "", fuel.get("fuel_source_unit"), fuel.get("fuel_source_type"))
            return Response(json, status=status.HTTP_201_CREATED, content_type=cls.content_json)
        except Exception as err:
            error = {"error":f"Something went wrong {err}"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type=cls.content_json)

    """get token form auth header

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param request: http request with bearer token
        :type request: request
        :returns: token
        :rtype: str
    """
    @classmethod
    def get_token_from_header(cls, request):
        auth_header = request.headers.get('Authorization')
        
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            return token
        return ""

    """get carbon score from request for token or session id

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param request: http request with bearer token
        :type request: request
        :param session_id: token or session_id from request
        :type session_id: str
        :returns: score as json
        :rtype: json
    """
    @classmethod
    def get_carbon_score_from_request(cls, response, session_id):
        try:
            resp_json = response.data
            data = resp_json.get('data')
            attributes = data.get('attributes')

            carbon_g = attributes.get('carbon_g')
            carbon_kg = attributes.get('carbon_kg')
            carbon_lb = attributes.get('carbon_lb')
            carbon_mt = attributes.get('carbon_mt')

            ds = DomainServiceInterface()
            score = ds.create_carbon_score(Decimal(carbon_g), Decimal(carbon_kg), Decimal(carbon_lb), Decimal(carbon_mt), session_id)
            
            return ds.convert_score_to_json(score)
        except Exception as err:
            return {'error': f'something went wrong {err}'}

    """get carbon score sum from database with given unit

        :author: Raphael Wudy (raphael.wudy@stud.th-rosenheim.de)
        :param token: identifiyer for your database sum up
        :type token: str
        :param unit: unit you want your score displayed in
        :type unit: str
        :returns: database response as json
    """
    @classmethod
    def get_carbon_score_for_token(cls, token: str, unit: str):
        dbs = DatabaseServiceInterface()
        score = dbs.sum_carbon_score_for_session_id(token, unit)
        json = {f"score_{unit}":score}
        return Response(json, status=status.HTTP_200_OK, content_type=cls.content_json)