from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from SessionsPerStation.views import *

class TestUrls(SimpleTestCase):

    def test_SPS1_url(self):
        url = reverse('SessionsPerStation:SPS1', args=['1'])
        self.assertEquals(resolve(url).func.view_class, SPS_stationID)

    def test_SPS2_url(self):
        url = reverse('SessionsPerStation:SPS2', args=['1','20210105'])
        self.assertEquals(resolve(url).func.view_class, SPS_stationID_Start)
    
    def test_SPS3_url(self):
        url = reverse('SessionsPerStation:SPS3', args=['1','20210105','20210201'])
        self.assertEquals(resolve(url).func.view_class, SPS_stationID_Start_Finish)