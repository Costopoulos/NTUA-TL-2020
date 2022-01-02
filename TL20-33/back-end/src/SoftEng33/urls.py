"""SoftEng33 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from pages.views import *
from pages import views
from payment.views import payment_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path('evcharge/api/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('evcharge/api/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('evcharge/api/register/', RegisterView.as_view()),
    #path('evcharge/api/scalablelogin/', LoginView.as_view()),
    #path('evcharge/api/scalableuser/', UserView.as_view()),
    #path('evcharge/api/scalablelogout/', LogoutView.as_view()),
    path('evcharge/api/djangoadmin/', admin.site.urls),
    path('evcharge/api/SessionsPerPoint/', include('SessionsPerPoint.urls')),
    path('evcharge/api/SessionsPerStation/', include('SessionsPerStation.urls')),
    path('evcharge/api/SessionsPerEV/', include('SessionsPerEV.urls')),
    path('evcharge/api/SessionsPerProvider/', include('SessionsPerProvider.urls')),
    path('evcharge/api/admin/', include('admin.urls')),
    path('evcharge/api/', include('pages.urls')),
    path('evcharge/api/payment/', payment_view, name='payment'),
    path('evcharge/api/pleasework/', include('pleasework.urls')),
    #path('evcharge/api/login', MyLoginView.as_view(), name='mylogin'),
    #path('evcharge/api/myuserview/', MyUserView.as_view()),
    #path('evcharge/api/logout', MyLogoutView.as_view(), name='mylogout'),
    #path('evcharge/api/isadmincheck/', IsAdminCheck.as_view(), name='isadmincheck'),
    #path('evcharge/api/noobadmincheck/', IsAdminCheck.as_view()),
]
