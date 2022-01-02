from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from SessionsPerEV.views import *

class TestUrls(SimpleTestCase):

    def test_SPS1_url(self):
        url = reverse('SessionsPerEV:SPEV1', args=['1'])
        self.assertEquals(resolve(url).func.view_class, SPEV_vehicleID)

    def test_SPS2_url(self):
        url = reverse('SessionsPerEV:SPEV2', args=['1','20210105'])
        self.assertEquals(resolve(url).func.view_class, SPEV_vehicleID_Start)
    
    def test_SPS3_url(self):
        url = reverse('SessionsPerEV:SPEV3', args=['1','20210105','20210201'])
        self.assertEquals(resolve(url).func.view_class, SPEV_vehicleID_Start_Finish)