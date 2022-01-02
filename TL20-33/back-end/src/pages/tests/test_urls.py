from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from pages.views import *

class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('mylogin')
        self.assertEquals(resolve(url).func.view_class, MyLoginView)

    def test_logout_url(self):
        url = reverse('mylogout')
        self.assertEquals(resolve(url).func.view_class, MyLogoutView)
    
    def test_isadmincheck_url(self):
        url = reverse('isadmincheck')
        self.assertEquals(resolve(url).func.view_class, IsAdminCheck)