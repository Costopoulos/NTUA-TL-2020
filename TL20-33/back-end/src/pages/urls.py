from django.urls import path

from .views import *
urlpatterns = [
    path('login', MyLoginView.as_view(), name='mylogin'),
    path('myuserview/', MyUserView.as_view()),
    path('logout', MyLogoutView.as_view(), name='mylogout'),
    path('isadmincheck/', IsAdminCheck.as_view(), name='isadmincheck'),
    path('noobadmincheck/', IsAdminCheck.as_view()),
]