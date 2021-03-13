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


class SPPr_NoArgs(APIView):
    
    def get(self, request):
        result = EnergyProvider.objects.all().count()
        return Response(result)

# in contrast to the others this gives back json object, not json array
def getJsonObject(objects, model):
        list=[]
        for object in objects:
            # print(object)
            temp={}
            for field in model._meta.fields:
                fieldname = field.get_attname_column()
                fieldobj = model._meta.get_field(fieldname[0])
                # print("------>" + str(fieldobj))
                value = fieldobj.value_from_object(object)
                temp[fieldname[1]] = value
            list.append(temp)
        dict = {}
        for i, sub_dict in enumerate(list):
            dict[i] = sub_dict
        return json.loads(json.dumps(dict, indent=4, sort_keys=True, default=str))


class SPPr_providerID(APIView):

    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request, provider_id):
        if os.path.exists("softeng20bAPI.token"):
            if os.stat("softeng20bAPI.token").st_size != 0:
                rawObj1 = Charging.objects.raw("SELECT * FROM charging INNER JOIN station ON station.Station_id = charging.Station_id WHERE Energy_Provider_id = '" + str(provider_id) + "'")
                jsonObj1 = getJsonObject(rawObj1, Charging) # make RawQuserySet object into json
                rawObj2 = Station.objects.raw("SELECT * FROM station INNER JOIN charging ON station.Station_id = charging.Station_id WHERE Energy_Provider_id = '" + str(provider_id) + "'")
                jsonObj2 = getJsonObject(rawObj2, Station) # make RawQuserySet object into json

                # merge json objects
                for i in jsonObj1:
                    jsonObj1[i].update(jsonObj2[i])

                # make into json array
                dictlist = []
                for key, value in jsonObj1.items():
                    temp = value
                    dictlist.append(temp)  

                if len(dictlist) == 0:
                    return Response({"No data": "There is no data for the filter you have provided"}, status=status.HTTP_402_PAYMENT_REQUIRED)
                return Response(dictlist)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Not Authorized": "Please login first"}, status=status.HTTP_401_UNAUTHORIZED)



class SPPr_providerID_Start(APIView):

    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request, provider_id, start):
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
                
                # Run queries
                rawObj1 = Charging.objects.raw("SELECT * FROM charging INNER JOIN station ON station.Station_id = charging.Station_id WHERE Energy_Provider_id = '" + str(provider_id) + "' AND Start >= '" + startString + "'")
                jsonObj1 = getJsonObject(rawObj1, Charging) # make RawQuserySet object into json
                rawObj2 = Station.objects.raw("SELECT * FROM station INNER JOIN charging ON station.Station_id = charging.Station_id WHERE Energy_Provider_id = '" + str(provider_id) + "' AND Start >= '" + startString + "'")
                jsonObj2 = getJsonObject(rawObj2, Station) # make RawQuserySet object into json

                # merge json objects
                for i in jsonObj1:
                    jsonObj1[i].update(jsonObj2[i])

                # make into json array
                dictlist = []
                for key, value in jsonObj1.items():
                    temp = value
                    dictlist.append(temp)  

                if len(dictlist) == 0:
                    return Response({"No data": "There is no data for the filter you have provided"}, status=status.HTTP_402_PAYMENT_REQUIRED)
                return Response(dictlist)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Not Authorized": "Please login first"}, status=status.HTTP_401_UNAUTHORIZED)
    


class SPPr_providerID_Start_Finish(APIView):

    renderer_classes = [JSONRenderer, CSVRenderer]
    def get(self, request, provider_id, start, finish):
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
                
                # Run queries
                rawObj1 = Charging.objects.raw("SELECT * FROM charging INNER JOIN station ON station.Station_id = charging.Station_id WHERE Energy_Provider_id = '" + str(provider_id)  + "' AND Start >= '" + startString + "' AND Finish <= '" + finishString + "'")
                jsonObj1 = getJsonObject(rawObj1, Charging) # make RawQuserySet object into json
                rawObj2 = Station.objects.raw("SELECT * FROM station INNER JOIN charging ON station.Station_id = charging.Station_id WHERE Energy_Provider_id = '" + str(provider_id)  + "' AND Start >= '" + startString + "' AND Finish <= '" + finishString + "'")
                jsonObj2 = getJsonObject(rawObj2, Station) # make RawQuserySet object into json

                # merge json objects
                for i in jsonObj1:
                    jsonObj1[i].update(jsonObj2[i])

                # make into json array
                dictlist = []
                for key, value in jsonObj1.items():
                    temp = value
                    dictlist.append(temp)  

                if len(dictlist) == 0:
                    return Response({"No data": "There is no data for the filter you have provided"}, status=status.HTTP_402_PAYMENT_REQUIRED)
                return Response(dictlist)
            else:
                return Response({"Not Authorized": "You must login first"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"Not Authorized": "Please login first"}, status=status.HTTP_401_UNAUTHORIZED)

