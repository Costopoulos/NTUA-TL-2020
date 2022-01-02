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
    SPPr_NoArgs,
    SPPr_providerID,
    SPPr_providerID_Start, 
    SPPr_providerID_Start_Finish,
)

app_name = "SessionsPerProvider"
urlpatterns = [

    path('', SPPr_NoArgs.as_view(), name='SSPr_NoArgs'),
    path('<int:provider_id>', SPPr_providerID.as_view(), name='SSPr1'),
    path('<int:provider_id>/<int:start>', SPPr_providerID_Start.as_view(), name='SSPr2'),
    path('<int:provider_id>/<int:start>/<int:finish>', SPPr_providerID_Start_Finish.as_view(), name='SSPr3'),
]
