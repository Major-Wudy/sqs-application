from django.urls import path, include
from . import views
from . import api
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    #path("", views.index, name="index"),
    path('create/electricity/', api.create_electricity),
    path('get/estimate/electricity/', api.get_estimate_electricity),
    path('create/flight/', api.create_flight),
    #path('get/estimate/flight/', views.postData),
    path('create/shipping/', api.create_shipping),
    #path('get/estimate/shipping/', views.postData),
    path('create/fuel/', api.create_fuel),
    #path('get/estimate/fuel/', views.postData),
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]