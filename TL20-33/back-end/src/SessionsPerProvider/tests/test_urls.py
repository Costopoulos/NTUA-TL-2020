from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from SessionsPerProvider.views import *

class TestUrls(SimpleTestCase):

    def test_SPS1_url(self):
        url = reverse('SessionsPerProvider:SSPr1', args=['1'])
        self.assertEquals(resolve(url).func.view_class, SPPr_providerID)

    def test_SPS2_url(self):
        url = reverse('SessionsPerProvider:SSPr2', args=['1','20210105'])
        self.assertEquals(resolve(url).func.view_class, SPPr_providerID_Start)
    
    def test_SPS3_url(self):
        url = reverse('SessionsPerProvider:SSPr3', args=['1','20210105','20210201'])
        self.assertEquals(resolve(url).func.view_class, SPPr_providerID_Start_Finish)