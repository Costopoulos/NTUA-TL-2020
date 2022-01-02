from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from pages.views import *
from pages.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.cli = Client()
        self.users_url = reverse('ouradmin:WatchUsers', args=['George'])
        self.usermod_url = reverse('ouradmin:ModifyAddUsers', args=['admin', 'petrol4ever'])
        
        user1 = get_user_model().objects.create(
            username='George', 
            password='mole', 
            card_id = 300,
            points = 123
        )

    def test_users_GET(self):

        response = self.cli.get(self.users_url)
        #print(response.content)
        #print(response.content[0]) #points
        self.assertEquals(response.status_code, 200)
        #self.assertEquals(response.content[0], 123) #works

    def test_usermod_POST(self):
        
        response = self.cli.post(self.usermod_url, {'username': 'admin', 'password': 'petrol4ever'})
        self.assertEquals(response.status_code, 200)
        #print(response.content) -> message: user added successfully
        
        
    
