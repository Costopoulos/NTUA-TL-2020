from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from pleasework.models import *

class TestModels(TestCase):

    def setUp(self):
        self.model1 = User.objects.create(
            username = 'sela',
            password = 'ay',
            card_id = 432
        )

    def testmodelUser(self):
        self.assertEquals(self.model1.points, 0)
        self.assertEquals(self.model1.username, 'sela')
        self.assertEquals(self.model1.password, 'ay')
        self.assertEquals(self.model1.card_id, 432)
        self.assertEquals(self.model1.first_name, '')