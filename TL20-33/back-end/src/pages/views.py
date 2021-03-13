from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
#import requests
#import sys
#import datetime
from .forms import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from .models import *
# from django.contrib.gis.geos import Point
# from django.contrib.gis.measure import Distance
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.gis.measure import D
from django.http import HttpResponse
from django import template

from rest_framework.authtoken.models import Token
AUTH_TOKEN_LABEL = 'HTTP_X_OBSERVATORY_AUTH'
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework_csv.renderers import JSONRenderer, CSVRenderer



from django.contrib.auth import get_user_model
User = get_user_model()



def home_view(request, *args, **kwargs):
	#print(args,kwargs) 
	print(request.user)
	return render(request, "home.html", {})

# from django.contrib.auth.models import User
# from rest_framework import authentication
# from rest_framework import exceptions

class ViewUsers(APIView):
    template_name = "users.html"
    
    def get(self, request):
        obj = User.objects.all()
        json = getJsonObject(obj, User) #this for json, dont need it atm
        return HttpResponse(json)

# class ExampleAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('HTTP_X_USERNAME')
#         if not username:
#             return None

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')

#         return (user, None)

# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.models import User

# class HelloView(APIView): #this can do a json object as well by ?format=json
#     #permission_classes = (IsAuthenticated,) 
#     def get(self, request):#, username, password):
#         #user = User.objects.post(username=username)
#         #password = User.objects.get(password=password)
#         content = {
#             'message': 'Hello, World!',
#             #'username': user, #try with post
#             #'password': password,
#         }
#         return Response(content)#render(request, content) #Json

# class HelloView(APIView): 
#     def post(request, token=None):#token=None #, username, password):
#         #if request.method == 'POST':
#         f = UserLoginForm(request.POST)
#         #if f.is_valid():
#         username = f.cleaned_data['user']
#         password = f.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#         #token =
#         print(user) 
#         token, created = Token.objects.get_or_create(user=user)
#         print(token)
#         content = {
#             'message': 'Hello, World!',
#             'token' : token,
#             'user' : user,
#         }
#         return Response(content)#render(request, content) #Json
#         #return render(request, content)


class HelloView(APIView): #this can do a json object as well by ?format=json
    #permission_classes = (IsAuthenticated,) 
    def post(self, request, token=None, user=None):#, username, password):
        if request.method == 'POST':
            f = UserLoginForm(request.POST)
            if f.is_valid():
                username = f.cleaned_data['user']
                password = f.cleaned_data['password']
    
                user = authenticate(username=username, password=password)
                #token = 
                token, created = Token.objects.get_or_create(user=user)
                print(token, created) #this is correct
            content = {
                'message': 'Hello, World!',
                'token' : token,
                'user' : user,
            }
        return Response(content)#render(request, content) #Json


    # def post(self, request, token):
    	
    # 	# HttpRequest.POST
    # 	token = request.POST.get('token')
    # 	context = {
    # 		'token' : token,
    # 	}
    # 	return render(request, context)
    	# data = {
    	# 	'username' : user.username,
    	# 	'password' : user.password,
    	# }
    	# URL = 'login'
    	# return render(request, data)

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

def userslist(request):
    users = User.objects.all()
    print(users)
    ##print(connection.queries)
    return render(request, 'temp.html', {'data':users})

class Best_Login (APIView): #Bad
    def post(self, request, token=None):
        f = UserLoginForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data['user']
            password = f.cleaned_data['password']
            user = User.objects("SELECT * from user WHERE username = '" + username + "' AND password = '" + password + "'")
            token, created = Token.objects.get_or_create(user=user)
            #json = getJsonObject(obj, User)
            tokendict = {'token': token.key}
            if user is not None:
                print('login success') #terminal
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Συνδεθήκατε με επιτυχία!') #REDIRECT TO A SUCCESS PAGE
                    #return render(request, 'home.html', {'token':tokendict})#JsonResponse(tokendict)#Response({'token':tokendict})#render(request, 'home.html', {'token':tokendict}) #index, 'token':token, home.html
                    return HttpResponse({'token':tokendict})
            else:
                print('login failed')

# def signup(request):
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        #return 

class LoginView(APIView):
    # def handlefile(f):
    #     with open('')

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        #print('reaches') #does reach
        user = get_user_model().objects.filter(username=username).first() #User instead of getusr
        #print(type(user)) #does not reach, user model has error
        if user is None:
            raise AuthenticationFailed('User not found')

        userpass = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].password

        if not password == userpass:
            raise AuthenticationFailed('Incorrect password')
        # if not user['password']:
        #     raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        # tokendict = {
        #     'token': token,
        # }

        response = Response()
        response.set_cookie(key='token', value=token, httponly=True) #key='token'
        response.data = {
            'token': token
        }

        isadmin = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].is_staff
        #isadmin perfectly working

        if isadmin:
            #write in localhost:8765/evcharge/api/admin.token
            #adminfile = open('admin.token', 'x')
            adminfile = open('admin.token', 'r+')
            adminfile.write(token)
            adminfile.close()
        else:
            #write in localhost:8765/evcharge/api/softeng20bAPI.token
            #with open('localhost:8765/evcharge/api/softeng20bAPI.token', 'wb+') as destination:
            #    destination.write(tokendict)
            #APItoken = open('softeng20bAPI.token', 'x')
            APItoken = open('softeng20bAPI.token', 'r+')
            APItoken.write(token)
            APItoken.close()
            pass

        return response

        #return Response(tokendict)

        # return Response({
        #     #'message': 'success',
        #     #'isadmin': isadmin,
        #     'token': token,
        # })

class MyLoginView(APIView):
    # def handlefile(f):
    #     with open('')
    renderer_classes = [JSONRenderer, CSVRenderer]
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = get_user_model().objects.filter(username=username).first() #User instead of getusr
        
        #user = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].username
        
        if user is None:
            raise AuthenticationFailed('User not found')

        userpass = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].password

        if not password == userpass:
            raise AuthenticationFailed('Incorrect password')
        # if not user['password']:
        #     raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        # tokendict = {
        #     'token': token,
        # }

        # response = Response()
        # response.set_cookie(key='token', value=token, httponly=True) #key='token'
        # response.data = {
        #     'token': token
        # }

        isadmin = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].is_staff

        #write in localhost:8765/evcharge/api/softeng20bAPI.token
        #with open('localhost:8765/evcharge/api/softeng20bAPI.token', 'wb+') as destination:
        #    destination.write(tokendict)


        if not os.path.exists("softeng20bAPI.token"):
            APItoken = open('softeng20bAPI.token', 'x')
            APItoken = open('softeng20bAPI.token', 'r+')
            APItoken.write(token)
            APItoken.close()
        
        else:
            return Response({
                'message':'someone is already logged in'
            })

        #return response

        return Response({
            #'message': 'success',
            #'isadmin': isadmin,
            'token': token
        })

class MyUserView(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request):
        #token = request.COOKIES.get('token')
        header = 'HTTP_X_OBSERVATORY_AUTH'
        #token = header.get['data']
        #token = request.data['token']
        #token = request.data.get['token']
        token = request.META.get(header)

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = get_user_model().objects.filter(user_id=payload['id']).first()
        print(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class IsAdminCheck(APIView):
    def get(self, request):
        # header = 'HTTP_X_OBSERVATORY_AUTH'
        # token = request.META.get(header)

        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                with open ('softeng20bAPI.token', 'r') as destination:
                    token = destination.readlines()[0]
                    #print(token)
                    #print(type(token))
            else:
                return Response({
                    'message':'user was not logged in'
                })
        else:
            return Response({
                'message':'login first please'
            })


        #isadmin = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].is_staff

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = get_user_model().objects.filter(user_id=payload['id']).first()
        #print(user)
        serializer = UserSerializer(user)
        username = serializer.data['username']
        #print("username is ")
        #print(username)
        if username == "admin":
            return Response(True) 
        else:
            return Response(False)

def checkadmin(request):
    if os.path.exists("softeng20bAPI.token"):
        if os.stat("softeng20bAPI.token").st_size != 0:
            with open ('softeng20bAPI.token', 'r') as destination:
                token = destination.readlines()[0]
                #print(token)
                #print(type(token))
        else:
            return Response({
                'message':'user was not logged in'
            })
    else:
        return Response({
            'message':'login first please'
        })


        #isadmin = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].is_staff

    if not token:
        raise AuthenticationFailed('Unauthenticated')
    
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')
    
    user = get_user_model().objects.filter(user_id=payload['id']).first()
    #print(user)
    serializer = UserSerializer(user)
    username = serializer.data['username']
    #print("username is ")
    #print(username)
    if username == "admin":
        return True
    else:
        return False

import os
from rest_framework import status
class MyLogoutView(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def post(self, request):
        # header = 'HTTP_X_OBSERVATORY_AUTH'
        # token = request.META.get(header)
        #print(token)
        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                os.remove("softeng20bAPI.token")
                # return Response({
                #     'message':'user logged out'
                # })
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "User already logged out"}, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        #token = request.data['token']#, wrong
        #token = request.data.get['token']

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            #payload = jwt.decode(token, 'secret', algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = get_user_model().objects.filter(user_id=payload['id']).first()
        print(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

#@api_view(('POST',))
#@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
class LogoutView(APIView):
    def post(self, request):
        #os.remove('')
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }
        # response.status = status.HTTP_200_OK
        response.status_code = 200
        return response

from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def empty_view(self):
    content = {'please move along': 'nothing to see here'}
    return Response(content, status=status.HTTP_404_NOT_FOUND)

@login_required(login_url='login')
def newlogout(request):
    logout(request)
    return render(request, 'home.html', {})

def newlogin(request, token=None):
    if request.method == 'POST':
        f = UserLoginForm(request.POST)
        if f.is_valid():
            #username = f.cleaned_data['user']
            #password = f.cleaned_data['password']
            username = request.POST.get('user')
            password = request.POST.get('password')

            
            user = authenticate(username=username, password=password)
            #user = User.objects("SELECT * from user WHERE username = 'username' AND password = 'password'" )
            #user = "SELECT * from user WHERE username = 'username' AND password = 'password'" 
            print(user)
            token, created = Token.objects.get_or_create(user=user)

            tokendict = {'token': token.key}
            print(token, created) #this is correct
            if user is not None:
                print('login success') #terminal
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Συνδεθήκατε με επιτυχία!') #REDIRECT TO A SUCCESS PAGE
                    return render(request, 'home.html', {'token':tokendict})#JsonResponse(tokendict)#Response({'token':tokendict})#render(request, 'home.html', {'token':tokendict}) #index, 'token':token, home.html
                
            else:
                print('login failed')
    else:
        f = UserLoginForm()
    return render(request, 'newsignin.html', {'form': f}) #signin.html

def signin(request, token=None):
    if request.method == 'POST':
        f = UserLoginForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data['user']
            password = f.cleaned_data['password']

            user = authenticate(username=username, password=password)
            #user = "SELECT id from user WHERE username = 'username' AND password = 'password'" 
            print(user)
            token, created = Token.objects.get_or_create(user=user)
            from django.core.serializers import serialize

            #serialize('json', token, cls=DjangoJSONEncoder)
            
            #tokendict = {'token': token}
            tokendict = {'token': token.key}
            

            #tokendict = json.dumps(tokendict)  WE NEED THHIS SOSSOSOSOSOSOSOSOSOSO
#
            

            #finaldict = json.loads(tokendict)

            #token = json.loads(token)
            #token.
            #Token.

            # from django.core.serializers import serialize

            # token = serialize('json', token)
            print(token, created) #this is correct
            if user is not None:
                print('login success') #terminal
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Συνδεθήκατε με επιτυχία!') #REDIRECT TO A SUCCESS PAGE
                    return render(request, 'home.html', {'token':tokendict})#JsonResponse(tokendict)#Response({'token':tokendict})#render(request, 'home.html', {'token':tokendict}) #index, 'token':token, home.html
                    #return HttpResponse(request) #not bad
                    
                    #return HttpResponse(request, {'token':tokendict})
                    #outdict = {'token': tokendict}
                    #html = '<html><body> Token is .</body></html>'
                    #html = '{% extends "base.html" %}{% block content %}Usertoken is {{outdict.key}}{% endblock %}'
                    #return HttpResponse(html)
                    #return HttpResponse(request, {'token':tokendict})
            #HttpResponse
            else:
                print('login failed')
    else:
        f = UserLoginForm()
    return render(request, 'newsignin.html', {'form': f}) #signin.html


def authenticate_token(request):
    """ Authenicate a user via token """
    try:
        user = Token.objects.get(key=request.META[AUTH_TOKEN_LABEL]).user
        return True
    except BaseException:
        return False

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             #'email': user.email
#         })

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        #def signin(request, token=None):
        if request.method == 'POST':
            f = UserLoginForm(request.POST)
            if f.is_valid():
                username = f.cleaned_data['user']
                password = f.cleaned_data['password']
                user = authenticate(username=username, password=password)
                token, created = Token.objects.get_or_create(user=user)
                print(token, created) #this is correct
                #serializer = self.serializer_class(data=request.data,
                                                   #context={'request': request})
                #serializer.is_valid(raise_exception=True)
                #user = serializer.validated_data['user']
                #token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token,
            'user_id': user.pk,
            #'email': user.email
        })

def signout(request):
    logout(request)
    return render(request, 'home.html', {})


import jwt,json
from rest_framework import views
from rest_framework.response import Response


class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:
            
            payload = {
                #'id': user.id,
                'username': user.username,
                #'email': user.email,
                'password': user.password,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return HttpResponse(
                json.dumps(jwt_token),
                status=200,
                content_type="application/json"
            )
        else:
            return Response(
                json.dumps({'Error': "Invalid credentials"}),
                status=400,
                content_type="application/json"
            )


# from rest_framework import status
# from rest_framework.generics import RetrieveAPIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest.app.user.serializers import UserLoginSerializer
# class UserLoginView(RetrieveAPIView):

#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         response = {
#             'success' : 'True',
#             'status code' : status.HTTP_200_OK,
#             'message': 'User logged in  successfully',
#             'token' : serializer.data['token'],
#             }
#         status_code = status.HTTP_200_OK

#         return Response(response, status=status_code)