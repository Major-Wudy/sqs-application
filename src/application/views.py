# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from application.services.infrastructure.api_service import BearerAuthentication
from application.services.infrastructure.api_service import ApiServices
from decimal import Decimal

@api_view(['GET'])
def getData(request):
    response = {'message':'dit it!'}
    return Response(response)

@api_view(['POST'])
def postData(request):
    post = {'message':'post request'}
    return Response(post)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_electricity(request):
    try:
        # JSON 
        # {
        #    "value":123,
        #    "country":"us"
        #    "state":"fl"
        #    "unit":"kwm"    
        # }
        data = request.data
        value = Decimal(data.get('value'))
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

        api = ApiServices()
        elec = api.create_electricity_from_post(value, country, state, unit)
        return Response(elec, status=status.HTTP_201_CREATED)
    except Exception as err:
        error = {"error":f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except TypeError as typeErr:
        error = {"error":f"Wrong parameter type: {typeErr}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_estimate_electricity(request):
    data = request.data
    api = ApiServices()
    estimate = api.get_estimate_for_electricity_from_post(data)
    return Response(estimate)

@api_view(['POST'])
def create_flight(request):
    post = {'message':'post create_electricity'}
    return Response(post)

@api_view(['POST'])
def get_estimate_flight(request):
    post = {'message':'post get_estimate_electricity'}
    return Response(post)

@api_view(['POST'])
def create_shipping(request):
    post = {'message':'post create_electricity'}
    return Response(post)

@api_view(['POST'])
def get_estimate_shipping(request):
    post = {'message':'post get_estimate_electricity'}
    return Response(post)

@api_view(['POST'])
def create_fuel(request):
    post = {'message':'post create_electricity'}
    return Response(post)

@api_view(['POST'])
def get_estimate_fuel(request):
    post = {'message':'post get_estimate_electricity'}
    return Response(post)
