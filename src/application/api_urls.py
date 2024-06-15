# register your api routes heres
from django.urls import path, include
from . import api
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('create/electricity/', api.create_electricity),
    path('estimate/electricity/', api.get_estimate_electricity),
    path('create/flight/', api.create_flight),
    path('estimate/flight/', api.get_estimate_flight),
    path('create/shipping/', api.create_shipping),
    path('estimate/shipping/', api.get_estimate_shipping),
    path('create/fuel/', api.create_fuel),
    path('estimate/fuel/', api.get_estimate_fuel),
    path('get/score/', api.get_carbon_score_for_token),
    # OpenAPI
    path('v1/schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    # Optional UI:
    path('v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    #path('v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
