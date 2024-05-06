from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    #path("", views.index, name="index"),
    path('', views.getData),
    path('post/', views.postData),
    path('create/electricity/', views.create_electricity),
    path('get/estimate/electricity/', views.get_estimate_electricity),
    #path('create/flight/', views.postData),
    #path('get/estimate/flight/', views.postData),
    #path('create/shipping/', views.postData),
    #path('get/estimate/shipping/', views.postData),
    #path('create/fuel/', views.postData),
    #path('get/estimate/fuel/', views.postData),
]