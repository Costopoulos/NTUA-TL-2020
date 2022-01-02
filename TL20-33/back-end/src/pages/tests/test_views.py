from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from pages.views import *
from pages.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.cli = Client()
        self.mylogin_url = reverse('mylogin')
        self.mylogout_url = reverse('mylogout')
        self.isadmin_url = reverse('isadmincheck')
        # self.user={
        #     'username': 'admin',
        #     'password': 'petrol4ever'
        # }
        get_user_model().objects.create(username='sela', password='ay', card_id = 300)


    def test_login_POST(self):
        response = self.cli.post(self.mylogin_url, {'username': 'sela', 'password': 'ay'})
        self.assertEquals(response.status_code, 200)


    def finaltest_logout_POST(self):
        #response = self.cli.post(self.mylogin_url, {'username': 'sela', 'password': 'ay'})
        if not os.path.exists("softeng20bAPI.token"):
            #raise AssertionError("400 or 401")
            Client.raise_request_exception = True #http error 400(not logged in) or 401(unauthorized: wrong credentials)
        else:
            response = self.cli.post(self.mylogout_url)
            self.assertEquals(response.status_code, 200)