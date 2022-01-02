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
    SPP_NoArgs,
    SPP_pointID,
    SPP_pointID_Start, 
    SPP_pointID_Start_Finish,
)

app_name = "SessionsPerPoint"
urlpatterns = [

    path('', SPP_NoArgs.as_view(), name='SPP_NoArgs'),
    path('<int:point_id>', SPP_pointID.as_view(), name='SPP1'),
    path('<int:point_id>/<int:start>', SPP_pointID_Start.as_view(), name='SPP2'),
    path('<int:point_id>/<int:start>/<int:finish>', SPP_pointID_Start_Finish.as_view(), name='SPP3'),
]
