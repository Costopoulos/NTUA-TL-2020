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
    SPS_NoArgs,
    SPS_stationID,
    SPS_stationID_Start, 
    SPS_stationID_Start_Finish,
)

app_name = "SessionsPerStation"
urlpatterns = [

    path('', SPS_NoArgs.as_view(), name='SPS_NoArgs'),
    path('<int:station_id>', SPS_stationID.as_view(), name='SPS1'),
    path('<int:station_id>/<int:start>', SPS_stationID_Start.as_view(), name='SPS2'),
    path('<int:station_id>/<int:start>/<int:finish>', SPS_stationID_Start_Finish.as_view(), name='SPS3'),
]
