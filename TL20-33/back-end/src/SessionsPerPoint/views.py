from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_csv.renderers import JSONRenderer, CSVRenderer
from rest_framework import status
import json
import datetime
from .models import *

# Create your views here.
from django.views.generic import (
    ListView,
)


class SPP_NoArgs(APIView):
    
    def get(self, request):
        result = Point.objects.all().count()
        return Response(result)

def getJsonObject(objects, model):
        list=[]
        for object in objects:
            # print(object)
            temp={}
            for field in model._meta.fields:
                fieldname = field.get_attname_column()
                fieldobj = model._meta.get_field(fieldname[0])
                value = fieldobj.value_from_object(object)
                temp[fieldname[1]] = value
            list.append(temp)
        dict = {}
        for i, sub_dict in enumerate(list):
            dict[i] = sub_dict
        dictlist = []
        for key, value in dict.items():
            temp = value
            dictlist.append(temp)    
        return json.loads(json.dumps(dictlist, indent=4, sort_keys=True, default=str))


class SPP_pointID(APIView):

    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request, point_id):
        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                rawObj = Charging.objects.raw("SELECT * FROM charging WHERE Point_id = '" + str(point_id) + "'")
                jsonObj = getJsonObject(rawObj, Charging) # make RawQuserySet object into json
                if len(jsonObj) == 0:
                    return Response({"No data": "There is no data for the filter you have provided"}, status=status.HTTP_402_PAYMENT_REQUIRED)
                return Response(jsonObj)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Not Authorized": "Please login first"}, status=status.HTTP_401_UNAUTHORIZED)




class SPP_pointID_Start(APIView):

    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request, point_id, start):
        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                # Create date string
                startString = str(start)
                
                # Check if date has correct format - must be 8-digit integer
                if len(startString) != 8:
                    return Response({"Bad Request": "Start Date must have the format: YYYYMMDD"}, status=status.HTTP_400_BAD_REQUEST)
        
                # Check if date exists/is valid
                try:
                    datetime.datetime(year=int(startString[0:4]), month=int(startString[4:6]), day=int(startString[6:8]))
                except:
                    startString = startString[0:4] + "-" + startString[4:6] + "-" + startString[6:8]
                    return Response({"Bad Request": "Start Date \'" + startString +"\' isn't valid"}, status=status.HTTP_400_BAD_REQUEST)
                
                # Make date into MySQL format
                startString = startString[0:4] + "-" + startString[4:6] + "-" + startString[6:8] + " 00:00:00"
                
                # Run query
                rawObj = Charging.objects.raw("SELECT * FROM charging WHERE Point_id = '" + str(point_id) + "' AND Start >= '" + startString + "'")
                jsonObj = getJsonObject(rawObj, Charging) # make RawQuserySet object into json
                if len(jsonObj) == 0:
                    return Response({"No data": "There is no data for the filter you have provided"}, status=status.HTTP_402_PAYMENT_REQUIRED)
                return Response(jsonObj)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Not Authorized": "Please login first"}, status=status.HTTP_401_UNAUTHORIZED)
    

import os
class SPP_pointID_Start_Finish(APIView):

    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request, point_id, start, finish):
        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                # Create date strings
                startString = str(start)
                finishString = str(finish)
                
                # Check if dates have correct format - must be 8-digit integer
                if len(startString) != 8:
                    return Response({"Bad Request": "Start Date must have the format: YYYYMMDD"}, status=status.HTTP_400_BAD_REQUEST)
                if len(finishString) != 8:
                    return Response({"Bad Request": "Finish Date must have the format: YYYYMMDD"}, status=status.HTTP_400_BAD_REQUEST)
                
                # Check if dates exist/are valid
                try:
                    datetime.datetime(year=int(startString[0:4]), month=int(startString[4:6]), day=int(startString[6:8]))
                except:
                    startString = startString[0:4] + "-" + startString[4:6] + "-" + startString[6:8]
                    return Response({"Bad Request": "Start Date \'" + startString +"\' isn't valid"}, status=status.HTTP_400_BAD_REQUEST)
                try:
                    datetime.datetime(year=int(finishString[0:4]), month=int(finishString[4:6]), day=int(finishString[6:8]))
                except:
                    finishString = finishString[0:4] + "-" + finishString[4:6] + "-" + finishString[6:8]
                    return Response({"Bad Request": "Finish Date \'" + finishString +"\' isn't valid"}, status=status.HTTP_400_BAD_REQUEST)
                
                # Check if Start Date < Finish Data
                if finish < start:
                    return Response({"Bad Request": "Start Date can't be after Finish Date"}, status=status.HTTP_400_BAD_REQUEST)
                
                # Make dates into MySQL format
                startString = startString[0:4] + "-" + startString[4:6] + "-" + startString[6:8] + " 00:00:00"
                finishString = finishString[0:4] + "-" + finishString[4:6] + "-" + finishString[6:8] + " 23:59:59"
                
                # Run query
                rawObj = Charging.objects.raw("SELECT * FROM charging WHERE Point_id = '" + str(point_id) + "' AND Start >= '" + startString + "' AND Finish <= '" + finishString + "'")
                jsonObj = getJsonObject(rawObj, Charging) # make RawQuserySet object into json
                if len(jsonObj) == 0:
                    return Response({"No data": "There is no data for the filter you have provided"}, status=status.HTTP_402_PAYMENT_REQUIRED)
                return Response(jsonObj)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Not Authorized": "Please login first"}, status=status.HTTP_401_UNAUTHORIZED)
