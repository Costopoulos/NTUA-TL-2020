# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Car(models.Model):
    car_id = models.IntegerField(db_column='Car_id', primary_key=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=45)  # Field name made lowercase.
    battery_size = models.IntegerField(db_column='Battery_Size')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'car'


class Charging(models.Model):
    charging_id = models.IntegerField(db_column='Charging_id', primary_key=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_id')  # Field name made lowercase.
    car = models.ForeignKey(Car, models.DO_NOTHING, db_column='Car_id')  # Field name made lowercase.
    payment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='Payment_id')  # Field name made lowercase.
    point = models.ForeignKey('Point', models.DO_NOTHING, db_column='Point_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'charging'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnergyProvider(models.Model):
    provider_id = models.IntegerField(db_column='Provider_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'energy_provider'


class Payment(models.Model):
    payment_id = models.IntegerField(db_column='Payment_id', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=45)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Point(models.Model):
    station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_id')  # Field name made lowercase.
    point_id = models.IntegerField(db_column='Point_id', primary_key=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'point'


class Station(models.Model):
    station_id = models.IntegerField(db_column='Station_id', primary_key=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    energy_provider = models.ForeignKey(EnergyProvider, models.DO_NOTHING, db_column='Energy_Provider_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'station'


class StationPhones(models.Model):
    station = models.ForeignKey(Station, models.DO_NOTHING, db_column='Station_id')  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'station_phones'


class User(models.Model):
    user_id = models.IntegerField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    card_id = models.IntegerField(db_column='Card_id')  # Field name made lowercase.
    wallet_id = models.CharField(db_column='Wallet_id', max_length=15)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class UserHasCar(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    car = models.ForeignKey(Car, models.DO_NOTHING, db_column='Car_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_has_car'


class UserPhones(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_phones'
