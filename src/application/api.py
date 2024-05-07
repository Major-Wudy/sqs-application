from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from application.services.infrastructure.api_service import BearerAuthentication
from application.services.infrastructure.api_service import ApiServices
from decimal import Decimal

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_electricity(request):
    """
        JSON 
        {
           "value":123,
           "country":"us"
           "state":"fl"
           "unit":"kwm"    
        }
    """
    data = request.data
    api = ApiServices()
    return api.create_electricity_from_post(data)
        

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def get_estimate_electricity(request):
    data = request.data
    api = ApiServices()
    return api.get_estimate_for_electricity_from_post(data)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_flight(request):
    """
        JSON 
        {
           "passengers":2,
           "legs":[{"destination":"DUB","depature":"MUC","class":"economy}],
           "distance_unit":"km"
        }
    """
    data = request.data
    api = ApiServices()
    return api.create_flight_from_post(data)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def get_estimate_flight(request):
    """
        JSON 
        {
           "passengers":2,
           "legs":[{"destination":"DUB","depature":"MUC","class":"economy}],
           "distance_unit":"km"
        }
    """
    data = request.data
    api = ApiServices()
    return api.get_estimate_for_flight_from_post(data)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_shipping(request):
    """
        JSON 
        {
            "weight_value": 123.45,
            "weight_unit": "kg",
            "distance_value": 500.01,
            "distance_unit": "km",
            "transport_method": "truck",
        }
    """
    data = request.data
    api = ApiServices()
    return api.create_shipping_from_post(data)

@api_view(['POST'])
def get_estimate_shipping(request):
    """
        JSON 
        {
            "weight_value": 123.45,
            "weight_unit": "kg",
            "distance_value": 500.01,
            "distance_unit": "km",
            "transport_method": "truck",
        }
    """
    data = request.data
    api = ApiServices()
    return api.get_estimate_for_shipping_from_post(data)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_fuel(request):
    """
        JSON 
        {
           "source":"Natural Gas",
           "value":500.01  
        }
    """
    data = request.data
    api = ApiServices()
    return api.create_fuel_from_post(data)

@api_view(['POST'])
def get_estimate_fuel(request):
    post = {'message':'post get_estimate_electricity'}
    return Response(post)
