from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from SessionsPerStation.views import *
from SessionsPerStation.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.cli = Client()
        self.SPS_stationID_url = reverse('SPS_stationID') + "/" + 3
        self.SPS_stationID_Start_url = reverse('SPS_stationID_Start') + "/" + str(3) + "/" + 20210106
        self.SPS_stationID_Start_Finish_url = reverse('SPS_stationID_Start_Finish')  + "/" + str(3) + "/" + 20210101 + "/" + 20210201
        Charging.objects.create(
            charging_id=1,
            start = '2021-01-05 14:25:36',
            finish = '2021-01-05 14:40:31',
            type = 'fast',
            user = 1,
            station = 3,
            car = 1,
            payment = 1,
            point = 74
        )
        Charging.objects.create(
            charging_id=2,
            start = '2021-02-05 15:26:37',
            finish = '2021-02-05 15:41:05',
            type = 'fast',
            user = 2,
            station = 3,
            car = 2,
            payment = 2,
            point = 62
        )


    # def test_login_POST(self):
    #     response = self.cli.post(self.mylogin_url, {'username': 'sela', 'password': 'ay'})
    #     self.assertEquals(response.status_code, 200)


    # def finaltest_logout_POST(self):
    #     #response = self.cli.post(self.mylogin_url, {'username': 'sela', 'password': 'ay'})
    #     if not os.path.exists("softeng20bAPI.token"):
    #         #raise AssertionError("400 or 401")
    #         Client.raise_request_exception = True #http error 400(not logged in) or 401(unauthorized: wrong credentials)
    #     else:
    #         response = self.cli.post(self.mylogout_url)
    #         self.assertEquals(response.status_code, 200)

    def test_SPS_stationID(self):
        response = self.cli.get(self.SPS_stationID_url)
        self.assertEquals(response.status_code, 200)

    def test_SPS_stationID_Start(self):
        response = self.cli.get(self.SPS_stationID_Start_url)
        self.assertEquals(response.status_code, 200)

    def test_SPS_stationID_Start_Finish_url(self):
        response = self.cli.get(self.SPS_stationID_Start_Finish_url)
        self.assertEquals(response.status_code, 200)
