from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique = True)
#     password = models.CharField(max_length=255)
#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class User(AbstractUser):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  #IntegerField # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=45, unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    card_id = models.IntegerField(db_column='Card_id')  # Field name made lowercase.
    wallet_id = models.CharField(db_column='Wallet_id', max_length=15)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', default=0)  # Field name made lowercase.
    id = None
    

    # class Meta:
    #     db_table = 'user'
    # class Meta:
    #     managed = False
    #     db_table = 'user'
    
    #user_id = models.IntegerField(primary_key=True)
    # username = models.CharField(max_length=45, unique=True)
    # password = models.CharField(max_length=45)  # 
    # email = models.CharField(max_length=45)  # Field 
    # card_id = models.IntegerField()  # Field name mad
    # wallet_id = models.CharField(max_length=15)  
    # points = models.IntegerField()  # Field name made 

    # class Meta:
    #     managed = False
    #     db_table = 'user'
