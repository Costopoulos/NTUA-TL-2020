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
# Create your views here.
def authlogin(request, token=None):
    if request.method == 'POST':
        f = UserLoginForm(request.POST)
        if f.is_valid():
            #username = f.cleaned_data['user']
            #password = f.cleaned_data['password']
            username = request.POST.get('user')
            password = request.POST.get('password')
            print('test')
            print(username)
            
            #user = authenticate(username=username, password=password)
            userpass = User.objects.raw("SELECT * FROM user WHERE Username = '" + username + "'")[0].password #SOS in raw queries you do the [0] cause it's a list
            
            if password == userpass:
                
                print(userpass)
                print('You are now logged in')
                #refresh = RefreshToken.for_user(username)
                #print(refresh)
                context = {
                    'user': username,
                    #'refresh': str(refresh),
                    #'access': str(refresh.access_token),
                }
                return render(request, 'dbloginsuccess.html', context)#JsonResponse(tokendict)#Response({'token':tokendict})#render(request, 'home.html', {'token':tokendict}) #index, 'token':token, home.html
                    
            else:
                print('Incorrect password')
    else:
        f = UserLoginForm()
    return render(request, 'newsignin.html', {'form': f}) #signin.html

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }