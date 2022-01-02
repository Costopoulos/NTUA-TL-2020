"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import (
    SPEV_NoArgs,
    SPEV_vehicleID,
    SPEV_vehicleID_Start, 
    SPEV_vehicleID_Start_Finish,
)

app_name = "SessionsPerEV"
urlpatterns = [

    path('', SPEV_NoArgs.as_view(), name='SPEV_NoArgs'),
    path('<int:vehicle_id>', SPEV_vehicleID.as_view(), name='SPEV1'),
    path('<int:vehicle_id>/<int:start>', SPEV_vehicleID_Start.as_view(), name='SPEV2'),
    path('<int:vehicle_id>/<int:start>/<int:finish>', SPEV_vehicleID_Start_Finish.as_view(), name='SPEV3'),
]
