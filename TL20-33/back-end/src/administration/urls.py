from django.urls import path

from .views import (
    ViewUsers,
    DetailedUser,
    DetailedUserWithString,
    #ModifyUser,
    Usermod,
    passwordchanged,
    NewViewUsers,
)
#app_name = "ouradmin"
urlpatterns = [
    path('users/', ViewUsers.as_view(), name='View_Users'),
    path('users/<int:user_id>', DetailedUser.as_view(), name='Detailed_User'),
    path('users/<str:username>', DetailedUserWithString.as_view(), name='Detailed_User_With_String'),
    #path('usermod/<str:username>/<str:password>', ModifyUser.as_view(), name='Modify_User'),
    path('usermod/', Usermod.as_view(), name='Usermod'),
    #path('usermod/<str:username>/<str:password>', Usermod.as_view(), name='Usermod'),
    path('usermod/success', passwordchanged, name='password_changed'),
    path('newusers/', NewViewUsers.as_view(), name='NewViewUsers'),
    # path('<int:vehicle_id>/<int:start>', SPEV_vehicleID_Start.as_view(), name='SPEV2'),
    # path('<int:vehicle_id>/<int:start>/<int:finish>', SPEV_vehicleID_Start_Finish.as_view(), name='SPEV3'),
]