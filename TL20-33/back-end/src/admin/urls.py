from django.urls import path

from .views import *
app_name = "ouradmin"
urlpatterns = [
    #path('users/', ViewUsers.as_view(), name='View_Users'),
    #path('users/<int:user_id>', DetailedUser.as_view(), name='Detailed_User'),
    #path('users/<str:username>', DetailedUserWithString.as_view(), name='Detailed_User_With_String'),
    #path('usermod/', Usermod.as_view(), name='Usermod'),
    #path('usermod/success', passwordchanged, name='password_changed'),
    #path('newusers/', NewViewUsers.as_view(), name='NewViewUsers'),
    path('users/<str:username>', WatchUsers.as_view(), name='WatchUsers'),
    path('usermod/<str:username>/<str:password>', ModifyAddUser.as_view(), name='ModifyAddUsers'),
    path('healthcheck', ConnectivityCheck.as_view(), name='ConnectivityCheck'),
    path('resetsessions', ResetSessions.as_view(), name='ResetSessions'),
    path('system/sessionsupd', UpdateSessions.as_view(), name='UpdateSessions'),
    path('addpayment/<slug:amount>/<str:method>/<str:bank>', AddPayment.as_view(), name='AddPayment'),
]
