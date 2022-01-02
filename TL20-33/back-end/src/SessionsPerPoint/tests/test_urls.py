from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from SessionsPerPoint.views import *

class TestUrls(SimpleTestCase):

    def test_SPS1_url(self):
        url = reverse('SessionsPerPoint:SPP1', args=['1'])
        self.assertEquals(resolve(url).func.view_class, SPP_pointID)

    def test_SPS2_url(self):
        url = reverse('SessionsPerPoint:SPP2', args=['1','20210105'])
        self.assertEquals(resolve(url).func.view_class, SPP_pointID_Start)
    
    def test_SPS3_url(self):
        url = reverse('SessionsPerPoint:SPP3', args=['1','20210105','20210201'])
        self.assertEquals(resolve(url).func.view_class, SPP_pointID_Start_Finish)