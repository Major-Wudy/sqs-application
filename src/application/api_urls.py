# register your api routes heres
from django.urls import path, include
from . import api
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('create/electricity/', api.create_electricity),
    path('get/estimate/electricity/', api.get_estimate_electricity),
    path('create/flight/', api.create_flight),
    path('get/estimate/flight/', api.get_estimate_flight),
    path('create/shipping/', api.create_shipping),
    path('create/fuel/', api.create_fuel),
    # OpenAPI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
