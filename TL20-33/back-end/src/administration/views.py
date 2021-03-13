from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import query
from django.shortcuts import render
from django.core.serializers import serialize
import json
from django.contrib.auth import authenticate
from .forms import NewPasswordForm

# Create your views here.
from .models import *

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
#from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

# class SPEV_NoArgs(ListView):
#     template_name = "SSPlist.html"
#     queryset = Charging.objects.all()
#     #query_PointOperator = "SELECT Operator FROM Point WHERE Point_id = " # based on implementation

def getJsonObject(objects, model):
        list=[]
        for object in objects:
            print(object) ########################################################
            temp={}
            for field in model._meta.fields:
                fieldname = field.get_attname_column()
                fieldobj = User._meta.get_field(fieldname[0]) #Charging._meta
                value = fieldobj.value_from_object(object)
                temp[fieldname[1]] = value
            list.append(temp)
        dict = {}
        for i, sub_dict in enumerate(list):
            dict[i] = sub_dict
        return json.dumps(dict, indent=4, sort_keys=True, default=str)

def passwordchanged(request):
    return render(request, "usermod.html", {})

class Usermod(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = 'success'
    template_name = 'newpassmodform.html'

# class ModifyUser(APIView):
#     template_name = "usermod.html"

#     # def get(self, request, username, password): #for mysql
#     #     obj = User.objects("SELECT Password from user WHERE Username = username AND Password = password") #tried with 'username' as well
#     #     json = getJsonObject(obj, User) #this for json, dont need it atm
#     #     return HttpResponse(json)

#     def post(self, request, username, password): #django auth, get
#         user = authenticate(username=username, password = password) #working for django
#         if user is not None:
#             #password change form (create it first)
#             #print(user)
#             f = NewPasswordForm(request.POST)
#             if f.is_valid():
#                 password = request.POST.get('password')
#                 print(user)
#                 u.set_password(password)
#                 return render(request, 'usermod.html', {})
#         f = NewPasswordForm()
#         return render(request, 'passmodform.html', {'form': f})      
#         #else:
#             #signup form (create it first) 
#         #return HttpResponse(password)

class NewViewUsers(ListView):
    template_name = "users.html"
    def get(self, request):
        queryset = User.objects.all()

class ViewUsers(APIView):
    template_name = "users.html"
    
    def get(self, request):
        obj = User.objects.all()
        json = getJsonObject(obj, User) #this for json, dont need it atm
        return HttpResponse(json)

        # mylist = []
        # outlist=[]
        # for object in obj:
        #     for field in User._meta.fields:
        #         fieldname = field.get_attname_column()
        #         fieldobj = User._meta.get_field(fieldname[0]) #Charging._meta
        #         value = fieldobj.value_from_object(object)
        #         mylist.append(str(value) + " ")
        #     #mylist = '\n'.join(mylist)
        #     outlist.append(mylist)
        # #return HttpResponse(mylist)
        # return HttpResponse(outlist)
        
class DetailedUserWithString(APIView):
    template_name = "oneuser.html"
    
    def get(self, request, username):
        #obj = User.objects.raw("SELECT * FROM user WHERE Username = username") 
        obj = User.objects.raw("SELECT * FROM user WHERE Username = '" + username + "'") 
        json = getJsonObject(obj, User) #this for json, dont need it atm
        return HttpResponse(json)

class DetailedUser(APIView):
    template_name = "oneuser.html"
    
    def get(self, request, user_id):
        obj = User.objects.raw("SELECT * FROM user WHERE User_id = '" + str(user_id) + "'") #str(user_id)
        json = getJsonObject(obj, User) #this for json, dont need it atm
        return HttpResponse(json)
        #return HttpResponse(obj.Username)

class SPEV_vehicleID(APIView):
    template_name = "points.html"

    def get(self, request, vehicle_id):
        obj = Charging.objects.raw("SELECT * FROM charging WHERE Car_id = '" + str(vehicle_id) + "'")
        json = getJsonObject(obj, Charging)
        return HttpResponse(json)


class SPEV_vehicleID_Start(APIView):
    template_name = "SPP2.html"

    def get(self, request, vehicle_id, start):
        start = str(start)
        start = start[0:4] + "-" + start[4:6] + "-" + start[6:8] + " 00:00:00"
        obj = Charging.objects.raw("SELECT * FROM charging WHERE Car_id = '" + str(vehicle_id) + "' AND Start >= '" + start + "'")
        json = getJsonObject(obj, Charging)
        return HttpResponse(json)
    
class SPEV_vehicleID_Start_Finish(APIView):
    template_name = "SPP2.html"

    def get(self, request, vehicle_id, start, finish):
        start = str(start)
        start = start[0:4] + "-" + start[4:6] + "-" + start[6:8] + " 00:00:00"
        finish = str(finish)
        finish = finish[0:4] + "-" + finish[4:6] + "-" + finish[6:8] + " 00:00:00"
        obj = Charging.objects.raw("SELECT * FROM charging WHERE Car_id = '" + str(vehicle_id) + "' AND Start >= '" + start + "' AND Finish <= '" + finish + "'")
        json = getJsonObject(obj, Charging)
        return HttpResponse(json)

