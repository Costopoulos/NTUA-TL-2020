from typing import MutableSequence
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework_csv.renderers import JSONRenderer, CSVRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import query
from django.shortcuts import render
from django.core.serializers import serialize
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
import json, requests, os
from django.contrib.auth import authenticate
from .forms import NewPasswordForm, UploadFileForm
from django.db import connection, connections
from django.db.utils import IntegrityError, OperationalError
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
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.db import connection
from datetime import datetime
from csv import reader
from django.contrib.auth import get_user_model
User = get_user_model()

def getJsonObject(objects, model):
        list=[]
        for object in objects:
            #print(object)
            temp={}
            for field in model._meta.fields:
                fieldname = field.get_attname_column()
                fieldobj = User._meta.get_field(fieldname[0]) 
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


class NewViewUsers(ListView):
    def get(self, request):
        queryset = User.objects.all()

class ViewUsers(APIView):
    def get(self, request):
        obj = User.objects.all()
        json = getJsonObject(obj, User) 
        return HttpResponse(json)
        
class DetailedUserWithString(APIView):
    def get(self, request, username):
        obj = User.objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'") 
        json = getJsonObject(obj, User) 
        return HttpResponse(json)

class WatchUsers(APIView):
    def get(self, request, username):
        answer = requests.get('http://localhost:8765/evcharge/api/noobadmincheck/')
        if answer.content == b'true':
            obj = User.objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")
            json = getJsonObject(obj, User) 
            return HttpResponse(json)
        else:
            return Response({"Not Authorized": "Log in as admin"}, status=status.HTTP_401_UNAUTHORIZED)

class ModifyAddUser(APIView):
    def post(self, request, username, password):
        answer = requests.get('http://localhost:8765/evcharge/api/noobadmincheck/') 
        if answer.content == b'true':
            user = User.objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")
            try:
                userobj = user[0]
            except IndexError:
                userobj = None
            if userobj is not None: #user exists
                userid = user[0].user_id
                #print(password)
                if user[0].password != password:
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE pleasework_user SET Password = '" + password + "' WHERE User_id = %s", [userid])
                    return Response({
                        'message': 'password changed',
                    })
                else:
                    return Response({
                        'message': 'you entered the same password'
                    })
            else: #user does not exist
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
            return Response({"Not Authorized": "Log in as admin"}, status=status.HTTP_401_UNAUTHORIZED)
        
class UpdateSessions(APIView):

    # parser_classes = [MultiPartParser]
    def post(self, request):
        answer = requests.get('http://localhost:8765/evcharge/api/isadmincheck/') 
        if answer.content == b'true':
            #data = pd.read_csv('test.csv')
            # print(request.data['file'])
            count = 0
            SessionsImported = 0
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(Charging_id) FROM charging")
                SessionsImported += cursor.fetchone()[0]
            upload_file = request.FILES['file']

            for i, line in enumerate(upload_file):
                if i == 0:
                    continue
                row = line.decode('utf-8').split(",")
                if(len(row) != 9):
                    continue # for last line
                count += 1
                # print(len(row))
                # print("INSERT INTO charging VALUE ("+row[1]+", '"+row[5]+"', '"+row[2]+"', '"+row[7]+"', "+row[8]+", "+row[6]+", "+row[0]+", "+row[3]+", "+row[4]+")")
                try:
                    connection.cursor().execute("INSERT INTO charging VALUE ("+row[1]+", '"+row[5]+"', '"+row[2]+"', '"+row[7]+"', "+row[8]+", "+row[6]+", "+row[0]+", "+row[3]+", "+row[4]+")")
                except:
                    return Response({"Bad Request": "Make sure given sessions aren't duplicate entries for already existing sessions IDs"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'SessionsInUploadedFile': count,
                'SessionsImported': SessionsImported,
                'TotalSessionsInDatabase' : count+SessionsImported
            })
                

        else:
            return Response({"Not Authorized": "Log in as admin"}, status=status.HTTP_401_UNAUTHORIZED)

class DetailedUser(APIView):
    def get(self, request, user_id):
        obj = User.objects.raw("SELECT * FROM user WHERE User_id = '" + str(user_id) + "'") 
        json = getJsonObject(obj, User) 
        return HttpResponse(json)

class ConnectivityCheck(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request):
        try:
            connection.ensure_connection()
        except OperationalError:
            return Response({'status':'failed'})
        
        return Response({'status':'OK'})


class AddPayment(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request, amount, method, bank):
        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                try:
                    with connection.cursor() as cursor:
                        paymentid = 1;
                        cursor.execute("SELECT COUNT(Payment_id) FROM payment")
                        paymentid += cursor.fetchone()[0]
                        cursor.execute("INSERT INTO payment VALUES ("+str(paymentid)+",'"+str(datetime.now())+"',"+str(amount).replace('-','.')+",'"+str(method)+"','"+str(bank)+"')")
                except OperationalError:
                    return Response({'status':'failed'})
        
                return Response({'status':'OK'})
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)

        


class ResetSessions(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def post(self, request):
        try:
            # delete all Charging Sessions
            Charging.objects.all().delete()
        except:
            return Response({'status':'failed'})
        try:
            userCount = 1
            with connection.cursor() as cursor:
                cursor.execute("SELECT MAX(User_id) FROM pleasework_user")
                userCount += cursor.fetchone()[0]
            print(userCount)
            walletID = userCount + 100
            connection.cursor().execute("INSERT INTO pleasework_user VALUE (NULL, 1, 'super', 'user', 1, 0, '" + str(datetime.now()) + "', "+str(userCount)+",'admin','petrol4ever','admin@gmail.com',"+str(userCount)+",'"+str(walletID)+"',750);")
        except:
            return Response({'status':'failed (admin already exists, but sessions are reset)'})

        
        return Response({'status':'OK'})

