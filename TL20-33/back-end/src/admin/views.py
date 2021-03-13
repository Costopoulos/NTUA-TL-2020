from typing import MutableSequence
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework_csv.renderers import JSONRenderer, CSVRenderer
from django.shortcuts import get_object_or_404
from django.db.models import query
from django.shortcuts import render
from django.core.serializers import serialize
import json
from django.contrib.auth import authenticate
from .forms import NewPasswordForm
from django.db import connection, connections
from django.db.utils import IntegrityError, OperationalError

# Create your views here.
from .models import *
from datetime import datetime

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
        obj = User.objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'") #user
        json = getJsonObject(obj, User) #this for json, dont need it atm
        return HttpResponse(json)

# class WatchUsers(APIView):
#     def post(self, request):
#         response = requests.post('localhost:8765/evcharge/api/isadmincheck/')
import requests
class WatchUsers(APIView):
    template_name = "oneuser.html"
    
    def get(self, request, username):
        #obj = User.objects.raw("SELECT * FROM user WHERE Username = username") 
        #answer = requests.post('http://localhost:8765/evcharge/api/isadmincheck/')
        #answer = requests.post('http://localhost:8765/evcharge/api/noobadmincheck/')
        #print(answer) #outputs <Response(405)>
        #print(answer.content)
        answer = requests.get('http://localhost:8765/evcharge/api/noobadmincheck/')
        #print("answer is ")
        #print(answer)
        #print("\n")
        #print("content is ")
        #print(answer.content)
        if answer.content == b'true':
            obj = User.objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'") #user
            json = getJsonObject(obj, User) #this for json, dont need it atm
            return HttpResponse(json)
        else:
            return Response({
                'message':'user does not have administration privileges'
            })

from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import connection
from datetime import datetime
class ModifyAddUser(APIView):
    template_name = "oneuser.html"
    
    def post(self, request, username, password):
        answer = requests.get('http://localhost:8765/evcharge/api/noobadmincheck/') #doesnt work
        print(answer)
        print(answer.content)
        if answer.content == b'true':
            # return Response({
            #     'message':'sela admin'
            # })
            user = User.objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")
            #print(user)
            #print(user[0])
            #print(len(user[0].user_id))
            try:
                userobj = user[0]
            except IndexError:
                userobj = None
            if userobj is not None: #user exists
                userid = user[0].user_id
                # return Response({
                #     'message': 'user exists',
                #     'id': userid
                # })
                print(password)
                if user[0].password != password:
                    #myquery = get_user_model().objects.raw("UPDATE pleasework_user SET Password = '" + password + "' WHERE User_id = '" + str(userid) + "'")#[0] #xwris [0]
                    
                    # getfromdb = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].password
                    # print(myquery)
                    # print(getfromdb)

                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE pleasework_user SET Password = '" + password + "' WHERE User_id = %s", [userid])

                    return Response({
                        'message': 'password changed',
                        #'id': userid
                    })
                else:
                    return Response({
                        'message': 'you entered the same password'
                    })
            else: #user does not exist
                # return Response({
                #     'message': 'userobj is null'
                # })
                #with connection.cursor() as cursor:
                #    cursor.execute("INSERT INTO pleasework_user VALUES (NULL, 0, '"+username+"', '"+username+"', 0, 0,  '" + str(datetime.now()) + "', 1,'"+username+"','"+password + "',NULL,1,'100',0)
                #userpass = get_user_model().objects.raw("INSERT INTO pleasework_user VALUES (NULL, 0, NULL, NULL, 0, 0, NULL, 102,'"+str(instance)+"','"+password+"','eu.erat@sitametluctus.net',102,'201',123)")
                userCount = 1
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(User_id) FROM pleasework_user")
                    userCount += cursor.fetchone()[0]
                #print(userCount)
                walletID = userCount + 100
                connection.cursor().execute("INSERT INTO pleasework_user VALUE (NULL, 0, '"+username+"', '"+username+"', 0, 0, '" + str(datetime.now()) + "', "+str(userCount)+",'"+username+"','"+password + "','"+username+"@"+username+".com',"+str(userCount)+",'"+str(walletID)+"',0);")
                return Response({
                    'message':'user added successfully'
                })

        else:
            return Response({
                'message':'user does not have administration privileges'
            })
        
    def get(self, request, username, password):
        #obj = User.objects.raw("SELECT * FROM user WHERE Username = username") 
        #answer = requests.post('http://localhost:8765/evcharge/api/isadmincheck/')
        #answer = requests.post('http://localhost:8765/evcharge/api/noobadmincheck/')
        #print(answer) #outputs <Response(405)>
        #print(answer.content)
        answer = requests.get('http://localhost:8765/evcharge/api/noobadmincheck/')
        #print("answer is ")
        #print(answer)
        #print("\n")
        #print("content is ")
        #print(answer.content)
        if answer.content == b'true':
            # return Response({
            #     'message':'sela admin'
            # })
            user = User.objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")
            #print(user)
            #print(user[0])
            #print(len(user[0].user_id))
            try:
                userobj = user[0]
            except IndexError:
                userobj = None
            if userobj is not None: #user exists
                userid = user[0].user_id
                # return Response({
                #     'message': 'user exists',
                #     'id': userid
                # })
                print(password)
                if user[0].password != password:
                    #myquery = get_user_model().objects.raw("UPDATE pleasework_user SET Password = '" + password + "' WHERE User_id = '" + str(userid) + "'")#[0] #xwris [0]
                    
                    # getfromdb = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].password
                    # print(myquery)
                    # print(getfromdb)

                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE pleasework_user SET Password = '" + password + "' WHERE User_id = %s", [userid])

                    return Response({
                        'message': 'password changed',
                        #'id': userid
                    })
                else:
                    return Response({
                        'message': 'you entered the same password'
                    })

            else: #user does not exist
                return Response({
                    'message': 'userobj is null'
                })
            # if userobj is not None: #user
            #     print("kalhspera")
            #     userid = user[0].user_id
            #     print(userid)
            #     if userid >= 1:
            #         return Response({
            #             'message': 'user exists'
            #         })
            #     else:
            #         return Response({
            #             'message': 'user does not exist'
            #         })
            # else:
            #     return Response({
            #         'message': 'userobj is null'
            #     })
        else:
            return Response({
                'message':'user does not have administration privileges'
            })

import pandas as pd
from csv import reader
class UpdateSessions(APIView):
    template_name = "oneuser.html"

    def post(self, request):
        answer = requests.get('http://localhost:8765/evcharge/api/noobadmincheck/') 
        print(answer)
        print(answer.content)
        if answer.content == b'true':
            #data = pd.read_csv('test.csv')
            count = 0
            SessionsImported = 0
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(Charging_id) FROM charging")
                SessionsImported += cursor.fetchone()[0]
            with open('test.csv', 'r') as myfile:
                next(myfile)
                data = reader(myfile)
                for row in data:
                    count += 1
                    connection.cursor().execute("INSERT INTO charging VALUE ("+row[1]+", '"+row[5]+"', '"+row[2]+"', '"+row[7]+"', "+row[8]+", "+row[6]+", "+row[0]+", "+row[3]+", "+row[4]+")")
            
            return Response({
                'SessionsInUploadedFile': count,
                'SessionsImported': SessionsImported,
                'TotalSessionsInDatabase' : count+SessionsImported
            })
                

        else:
            return Response({
                'message':'no administration privileges'
            })

def checkcsv(self, request):
    with open('test.csv', 'r') as myfile:
        data = reader(myfile)
        for row in data: #list from 0 to 8
            connection.cursor().execute("INSERT INTO charging VALUE ('"+row[1]+"', '"+row[5]+"', '"+row[2]+"', '"+row[7]+"', '"+row[8]+"', '"+row[6]+"', '"+row[0]+"', '"+row[3]+"', '"+row[4]+"'")
    return render(request, 'swta.html', {})

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


class ConnectivityCheck(APIView):

    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request):
        try:
            connection.ensure_connection()
        except OperationalError:
            return Response({'status':'failed'})
        
        return Response({'status':'OK'})


class ResetSessions(APIView):
    
    renderer_classes = [JSONRenderer, CSVRenderer]
    def post(self, request):
        try:
            # delete all Charging Sessions
            Charging.objects.all().delete()
            userCount = 1
            with connection.cursor() as cursor:
                cursor.execute("SELECT MAX(User_id) FROM pleasework_user")
                userCount += cursor.fetchone()[0]
            print(userCount)
            walletID = userCount + 100
            connection.cursor().execute("INSERT INTO pleasework_user VALUE (NULL, 1, 'super', 'user', 1, 0, '" + str(datetime.now()) + "', "+str(userCount)+",'admin','petrol4ever','admin@gmail.com',"+str(userCount)+",'"+str(walletID)+"',750);")
        except:
            return Response({'status':'failed'})
        
        return Response({'status':'OK'})

