from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
import os
from rest_framework import status
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import views
User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = get_user_model().objects.filter(username=username).first() #User instead of getuser
        if user is None:
            raise AuthenticationFailed('User not found')

        userpass = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].password

        if not password == userpass:
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='token', value=token, httponly=True) #key='token'
        response.data = {
            'token': token
        }

        isadmin = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].is_staff

        if isadmin:
            adminfile = open('admin.token', 'r+')
            adminfile.write(token)
            adminfile.close()
        else:
            APItoken = open('softeng20bAPI.token', 'r+')
            APItoken.write(token)
            APItoken.close()
            pass

        return response

class MyLoginView(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = get_user_model().objects.filter(username=username).first() #User instead of getuser
        
        #could also do user = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].username
        
        if user is None:
            raise AuthenticationFailed('User not found')

        userpass = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].password

        if not password == userpass:
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        # response = Response()
        # response.set_cookie(key='token', value=token, httponly=True) #key='token'
        # response.data = {
        #     'token': token
        # }

        isadmin = get_user_model().objects.raw("SELECT * FROM pleasework_user WHERE Username = '" + username + "'")[0].is_staff

        if not os.path.exists("softeng20bAPI.token"):
            APItoken = open('softeng20bAPI.token', 'x')
            APItoken = open('softeng20bAPI.token', 'r+')
            APItoken.write(token)
            APItoken.close()
        
        else:
            return Response({
                'message':'You are already logged in'
            })

        return Response({
            'token': token
        })

class MyUserView(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request):
        #token = request.COOKIES.get('token')
        header = 'HTTP_X_OBSERVATORY_AUTH'
        token = request.META.get(header)

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = get_user_model().objects.filter(user_id=payload['id']).first()
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
            else:
                return Response({
                    'message':'user was not logged in'
                })
        else:
            return Response({
                'message':'login first please'
            })

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = get_user_model().objects.filter(user_id=payload['id']).first()
        serializer = UserSerializer(user)
        username = serializer.data['username']
        if username == "admin":
            return Response(True) 
        else:
            return Response(False)

def checkadmin(request):
    if os.path.exists("softeng20bAPI.token"):
        if os.stat("softeng20bAPI.token").st_size != 0:
            with open ('softeng20bAPI.token', 'r') as destination:
                token = destination.readlines()[0]
        else:
            return Response({
                'message':'user was not logged in'
            })
    else:
        return Response({
            'message':'login first please'
        })

    if not token:
        raise AuthenticationFailed('Unauthenticated')
    
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')
    
    user = get_user_model().objects.filter(user_id=payload['id']).first()
    serializer = UserSerializer(user)
    username = serializer.data['username']
    if username == "admin":
        return True
    else:
        return False

class MyLogoutView(APIView):
    renderer_classes = [JSONRenderer, CSVRenderer]
    def post(self, request):
        # header = 'HTTP_X_OBSERVATORY_AUTH'
        # token = request.META.get(header)
        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                os.remove("softeng20bAPI.token")
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "User already logged out"}, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')

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

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }
        response.status_code = 200
        return response


def signin(request, token=None):
    if request.method == 'POST':
        f = UserLoginForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data['user']
            password = f.cleaned_data['password']

            user = authenticate(username=username, password=password) 
            print(user)
            token, created = Token.objects.get_or_create(user=user)
            from django.core.serializers import serialize

            #serialize('json', token, cls=DjangoJSONEncoder)
            
            tokendict = {'token': token.key}
            
            #print(token, created) 
            if user is not None:
                print('login success') #terminal
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Συνδεθήκατε με επιτυχία!') #REDIRECT TO A SUCCESS PAGE
                    return render(request, 'home.html', {'token':tokendict})
            else:
                print('login failed')
    else:
        f = UserLoginForm()
    return render(request, 'newsignin.html', {'form': f}) #signin.html


def signout(request):
    logout(request)
    return render(request, 'home.html', {})
