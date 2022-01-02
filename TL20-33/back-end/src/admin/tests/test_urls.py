from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from admin.views import *

class TestUrls(SimpleTestCase):

    def test_users_url(self):
        url = reverse('ouradmin:WatchUsers', args=['George'])#, args = ['George'])
        self.assertEquals(resolve(url).func.view_class, WatchUsers)

    def test_usermod_url(self):
        url = reverse('ouradmin:ModifyAddUsers', args=['George', 'molestie'])
        self.assertEquals(resolve(url).func.view_class, ModifyAddUser)

    def test_healthcheck_url(self):
        url = reverse('ouradmin:ConnectivityCheck')
        self.assertEquals(resolve(url).func.view_class, ConnectivityCheck)
    
    def test_resetsessions_url(self):
        url = reverse('ouradmin:ResetSessions')
        self.assertEquals(resolve(url).func.view_class, ResetSessions)
    
    def test_updsessions_url(self):
        url = reverse('ouradmin:UpdateSessions')
        self.assertEquals(resolve(url).func.view_class, UpdateSessions)