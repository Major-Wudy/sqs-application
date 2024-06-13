from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from application.services.infrastructure.api_service import BearerAuthentication
from application.services.infrastructure.api_service import ApiServices
from application.services.infrastructure_interface.database_interface import DatabaseServiceInterface
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
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)

        resp = api.create_electricity_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    description="get estimate carbon for electricity",
        request=[
            OpenApiCallback(name="estimate electricity", path="/api/get/estimate/electricity/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="electricity entity", status_codes="200",
                value={
                    "type": "electricity",
                    "electricity_unit": "kwh",
                    "electricity_value": "123.45",
                    "country": "us",
                    "state": "fl"
                    })
        ],
        responses={
            status.HTTP_201_CREATED: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                                "data": {
                                    "id": "ef065a14-651f-4323-a64a-83890348af22",
                                    "type": "estimate",
                                    "attributes": {
                                        "country": "us",
                                        "state": "fl",
                                        "electricity_unit": "kwh",
                                        "electricity_value": 123.45,
                                        "estimated_at": "2024-05-09T17:25:52.041Z",
                                        "carbon_g": 48937,
                                        "carbon_lb": 107.89,
                                        "carbon_kg": 48.94,
                                        "carbon_mt": 0.05
                                    }
                                }
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
def get_estimate_electricity(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)

        resp = api.get_estimate_for_electricity_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp 
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
                            "departure":"MUC",
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
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)

        resp = api.create_flight_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp 
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    description="get estimate carbon for flight",
        request=[
            OpenApiCallback(name="estimate flight", path="/api/get/estimate/flight/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="flight entity", status_codes="200",
                value={
                    "type": "flight",
                    "passengers": "2",
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
        responses={
            status.HTTP_201_CREATED: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                                "data": {
                                    "id": "42999c38-a2b7-48e5-9ec0-bc60a7d870c1",
                                    "type": "estimate",
                                    "attributes": {
                                        "passengers": 2,
                                        "legs": [
                                            {
                                                "departure_airport": "MUC",
                                                "destination_airport": "DUB",
                                                "cabin_class": "premium"
                                            }
                                        ],
                                        "distance_value": 1481.06,
                                        "distance_unit": "km",
                                        "estimated_at": "2024-05-09T17:29:36.986Z",
                                        "carbon_g": 391356,
                                        "carbon_lb": 862.79,
                                        "carbon_kg": 391.36,
                                        "carbon_mt": 0.39
                                    }
                                }
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
def get_estimate_flight(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)
        
        resp = api.get_estimate_for_flight_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp 
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
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)

        resp = api.create_shipping_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp 
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    description="get estimate carbon for shipping",
        request=[
            OpenApiCallback(name="estimate shipping", path="/api/get/estimate/shipping/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="shipping entity", status_codes="201",
                value={
                    "type": "shipping",
                    "weight_value": "123.45",
                    "weight_unit": "g",
                    "distance_value": "500.01",
                    "distance_unit": "km",
                    "transport_method": "plane"
                    })
        ],
        responses={
            status.HTTP_200_OK: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                                "data": {
                                    "id": "b4ac6ce9-ba1b-4ee4-b30e-b73e16465bfd",
                                    "type": "estimate",
                                    "attributes": {
                                        "distance_value": 500.01,
                                        "weight_unit": "g",
                                        "transport_method": "plane",
                                        "weight_value": 123.45,
                                        "distance_unit": "km",
                                        "estimated_at": "2024-05-09T17:18:01.418Z",
                                        "carbon_g": 37,
                                        "carbon_lb": 0.08,
                                        "carbon_kg": 0.04,
                                        "carbon_mt": 0.0
                                    }
                                }
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
def get_estimate_shipping(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)

        resp = api.get_estimate_for_shipping_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp 
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
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)

        resp = api.create_fuel_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp 
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    description="get estimate carbon for fuel",
        request=[
            OpenApiCallback(name="estimate fuel", path="/api/get/estimate/fuel/", decorator="requests"),
        ],
        examples=[
            OpenApiExample(name="fuel entity", status_codes="200",
                value={
                    "type": "fuel_combustion",
                    "fuel_source_type": "ng",
                    "fuel_source_unit": "thousand_cubic_feet",
                    "fuel_source_value": "500.00"
                    })
        ],
        responses={
            status.HTTP_201_CREATED: OpenApiResponse("Success",
                description="Success",
                examples=[
                    OpenApiExample(name="Success",
                        value={
                                "data": {
                                    "id": "97e1b97b-9c3b-4e87-b2f4-4c20131d162d",
                                    "type": "estimate",
                                    "attributes": {
                                        "fuel_source_type": "ng",
                                        "fuel_source_unit": "thousand_cubic_feet",
                                        "fuel_source_value": 500.0,
                                        "estimated_at": "2024-05-09T17:34:39.806Z",
                                        "carbon_g": 26560000,
                                        "carbon_lb": 58554.78,
                                        "carbon_kg": 26560.0,
                                        "carbon_mt": 26.56
                                    }
                                }
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
def get_estimate_fuel(request):
    try:
        data = request.data
        if not isinstance(data, dict):
            raise TypeError()

        api = ApiServices()
        token = api.get_token_from_header(request)
        dbs = DatabaseServiceInterface()
        if token:
            dbs.insert_request(data, token)

        resp = api.get_estimate_for_fuel_from_post(data)
        if resp:
            dbs.delete_request(token=token)
        return resp 
    except TypeError as err:
        error = {'error': f"request body does not contain valid json {err}"}
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        error = {'error': f"Something went wrong {err}"}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
