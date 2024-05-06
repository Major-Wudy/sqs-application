from django.urls import path, include
from . import views
from . import api
from django.conf import settings

urlpatterns = [
    #path("", views.index, name="index"),
    path('create/electricity/', api.create_electricity),
    path('get/estimate/electricity/', api.get_estimate_electricity),
    path('create/flight/', api.create_flight),
    #path('get/estimate/flight/', views.postData),
    path('create/shipping/', api.create_shipping),
    #path('get/estimate/shipping/', views.postData),
    #path('create/fuel/', views.postData),
    #path('get/estimate/fuel/', views.postData),
]