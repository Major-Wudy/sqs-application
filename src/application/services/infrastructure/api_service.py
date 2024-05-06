import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
application_dir = os.path.dirname(parent_dir)
src_dor = os.path.dirname(application_dir)

from rest_framework import authentication
from application.services.infrastructure.estimates_service import EstimatesService
from application.services.domain.electricity_service import ElectricityService
from decimal import Decimal
#import jsonpickle
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
    def create_electricity_from_post(cls, value: Decimal, country: str, state: str, unit: str) -> json:
        try:
            es = ElectricityService()
            elec = es.create_electricity_entity(Decimal(value), country, state, unit)
            return es.convert_electricity_entity_to_json(elec)
        except Exception as err:
            return {'error': f'could not create electricity entity. Check your post request. {err}'}

    @classmethod
    def get_estimate_for_electricity_from_post(cls, electricity: json):
        try:
            # ToDo check json for missing values and correct syntax

            es = EstimatesService()
            return es.get_estimate_for_electricity_use(Decimal(electricity.get("electricity_value")), electricity.get("country"), electricity.get("state"), electricity.get("electricity_unit"))
        except Exception as err:
            return {'error': f'could not create electricity entity. Check your post request. {err}'}
