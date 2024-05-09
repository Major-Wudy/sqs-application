from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from application.services.infrastructure.api_service import BearerAuthentication
from application.services.infrastructure.api_service import ApiServices
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse, OpenApiRequest, OpenApiCallback
from drf_spectacular.types import OpenApiTypes
from rest_framework import status


@extend_schema(
    description="create an electricity Object",
        request=[
            OpenApiCallback(name="electricity", path="/api/create/electricity/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="electricity input values", status_codes="200",
                value={
                    "value":100.5,
                    "country":"us",
                    "state":"fl",
                    "unit":"kwh"
                    })
        ],
        responses={
            status.HTTP_201_CREATED: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                            "type":"electricity",
                            "electricity_unit":"kwh",
                            "electricity_value":100.5,
                            "country":"us",
                            "state":"fl"
                            })
                    ],
                ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse("UnauthorizedError",
                description="UnauthorizedError",
                examples=[
                    OpenApiExample(name="UnauthorizedError",
                        value={
                            "detail":"Authentication credentials were not provided."
                            })
                    ],
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse("Bad Request",
                description="Bad Request",
                examples=[
                    OpenApiExample(name="Bad Request",
                        value={
                            "detail":"JSON parse error - Expecting property name enclosed in double quotes: line 2 column 16 (char 17)"
                            })
                    ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse("Internal Server Error",
                description="Internal Server Error",
                examples=[
                    OpenApiExample(name="Internal Server Error",
                        value={
                            "error":"Something went wrong"
                            })
                    ],
            ),
        }
    )
@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_electricity(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.create_electricity_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated]) 
def get_estimate_electricity(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.get_estimate_for_electricity_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema(
    description="create an flight object",
        request=[
            OpenApiCallback(name="flight", path="/api/create/flight/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="flight input values", status_codes="200",
                value={
                    "passengers":2,
                    "legs":[
                        {
                            "depature":"MUC",
                            "destination":"DUB",
                            "class":"premium"
                        }
                    ],
                    "distance_unit":"km"
                    })
        ],
        responses={
            status.HTTP_201_CREATED: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                            "type": "flight",
                            "passengers": 2,
                            "legs": [
                                {
                                    "departure_airport": "MUC",
                                    "destination_airport": "DUB",
                                    "cabin_class": "premium"
                                }
                            ],
                            "distance_unit": "km"
                            })
                    ],
                ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse("UnauthorizedError",
                description="UnauthorizedError",
                examples=[
                    OpenApiExample(name="UnauthorizedError",
                        value={
                            "detail":"Authentication credentials were not provided."
                            })
                    ],
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse("Bad Request",
                description="Bad Request",
                examples=[
                    OpenApiExample(name="Bad Request",
                        value={
                            "detail":"JSON parse error - Expecting property name enclosed in double quotes: line 2 column 16 (char 17)"
                            })
                    ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse("Internal Server Error",
                description="Internal Server Error",
                examples=[
                    OpenApiExample(name="Internal Server Error",
                        value={
                            "error":"Something went wrong"
                            })
                    ],
            ),
        }
    )
@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_flight(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.create_flight_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def get_estimate_flight(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.get_estimate_for_flight_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema(
    description="create an shipping object",
        request=[
            OpenApiCallback(name="shipping", path="/api/create/shipping/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="shipping input values", status_codes="200",
                value={
                    "weight_value":123.45,
                    "weight_unit": "g",
                    "distance_value": 500.01,
                    "distance_unit": "km",
                    "transport_method": "plane"
                    })
        ],
        responses={
            status.HTTP_201_CREATED: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                            "type": "shipping",
                            "weight_value": "123.45",
                            "weight_unit": "g",
                            "distance_value": "500.01",
                            "distance_unit": "km",
                            "transport_method": "plane"
                            })
                    ],
                ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse("UnauthorizedError",
                description="UnauthorizedError",
                examples=[
                    OpenApiExample(name="UnauthorizedError",
                        value={
                            "detail":"Authentication credentials were not provided."
                            })
                    ],
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse("Bad Request",
                description="Bad Request",
                examples=[
                    OpenApiExample(name="Bad Request",
                        value={
                            "detail":"JSON parse error - Expecting property name enclosed in double quotes: line 2 column 16 (char 17)"
                            })
                    ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse("Internal Server Error",
                description="Internal Server Error",
                examples=[
                    OpenApiExample(name="Internal Server Error",
                        value={
                            "error":"Something went wrong"
                            })
                    ],
            ),
        }
    )
@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_shipping(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.create_shipping_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def get_estimate_shipping(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.get_estimate_for_shipping_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@extend_schema(
    description="create an fuel object",
        request=[
            OpenApiCallback(name="shipping", path="/api/create/shipping/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="shipping input values", status_codes="200",
                value={
                    "source":"Natural Gas",
                    "value":500
                    })
        ],
        responses={
            status.HTTP_201_CREATED: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                            "type": "fuel_combustion",
                            "fuel_source_type": "ng",
                            "fuel_source_unit": "thousand_cubic_feet",
                            "fuel_source_value": 500.0
                            })
                    ],
                ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse("UnauthorizedError",
                description="UnauthorizedError",
                examples=[
                    OpenApiExample(name="UnauthorizedError",
                        value={
                            "detail":"Authentication credentials were not provided."
                            })
                    ],
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse("Bad Request",
                description="Bad Request",
                examples=[
                    OpenApiExample(name="Bad Request",
                        value={
                            "detail":"JSON parse error - Expecting property name enclosed in double quotes: line 2 column 16 (char 17)"
                            })
                    ],
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse("Internal Server Error",
                description="Internal Server Error",
                examples=[
                    OpenApiExample(name="Internal Server Error",
                        value={
                            "error":"Something went wrong"
                            })
                    ],
            ),
        }
    )
@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def create_fuel(request):
    try:   
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.create_fuel_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def get_estimate_fuel(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        return api.get_estimate_for_fuel_from_post(data)
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
