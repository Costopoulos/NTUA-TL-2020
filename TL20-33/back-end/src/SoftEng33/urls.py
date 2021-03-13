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
from authorization.views import *

from pages.views import home_view, HelloView, signin, login, Best_Login#, my_view#, ExampleAuthentication
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('evcharge/api/djangoadmin/', admin.site.urls),
    path('evcharge/api/api-auth/', include('rest_framework.urls')),
    path('evcharge/api/', home_view, name='home'),
    path('evcharge/api/signin/', signin, name='signin'), #views
    path('evcharge/api/hello/', HelloView.as_view(), name='hello'),
    path('evcharge/api/api-token-auth/', views.obtain_auth_token, name='api_token_auth'), #w/o views
    path('evcharge/api/api-token-auth2/', CustomAuthToken.as_view()),
    path('evcharge/api/djangologin/', newlogin, name='login'),
    path('evcharge/api/djangologout/', newlogout, name='logout'),
    #path(evcharge/api/'selalogout', include('django.contrib.auth.urls')),
    path('evcharge/api/SessionsPerPoint/', include('SessionsPerPoint.urls')),
    path('evcharge/api/SessionsPerStation/', include('SessionsPerStation.urls')),
    path('evcharge/api/SessionsPerEV/', include('SessionsPerEV.urls')),
    path('evcharge/api/SessionsPerProvider/', include('SessionsPerProvider.urls')),
    path('evcharge/api/admin/', include('admin.urls')),
    #path(evcharge/api/'admin/', include('administration.urls')),
    path('evcharge/api/payment/', payment_view, name='payment'),
    path('evcharge/api/users/', userslist, name='users'),
    path('evcharge/api/bestlogin/', Best_Login.as_view(), name='bestlogin'),
    path('evcharge/api/testusers/', ViewUsers.as_view(), name='testusers'),
    path('evcharge/api/authlogin/', authlogin, name='authlogin'),
    path('evcharge/api/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('evcharge/api/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('evcharge/api/pleasework/', include('pleasework.urls')),
    path('evcharge/api/register/', RegisterView.as_view()),
    path('evcharge/api/scalablelogin/', LoginView.as_view()),
    path('evcharge/api/scalableuser/', UserView.as_view()),
    path('evcharge/api/scalablelogout/', LogoutView.as_view()),
    path('isit404/', empty_view),
    path('evcharge/api/mylogin/', MyLoginView.as_view()),
    path('evcharge/api/myuserview/', MyUserView.as_view()),
    path('evcharge/api/mylogout/', MyLogoutView.as_view()),
    path('evcharge/api/isadmincheck/', IsAdminCheck.as_view()),
    path('evcharge/api/noobadmincheck/', IsAdminCheck.as_view()),

]
