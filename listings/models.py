from django.db import models
from general_models.models import Address
from user_profile.models import UserProfile

class Place(models.Model):
    address = models.OneToOneField(Address)
    num_beds = models.IntegerField(max_length=1, default=1)
    num_baths = models.IntegerField(max_length=1, default=1)
    num_stories = models.IntegerField(max_length=1, default=1)
      
class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    apt = models.IntegerField('Place')
    owner = models.OneToOneField(UserProfile)

    features = models.OneToOneField('Features')
    utilities = models.OneToOneField('Utilities')
    price = models.OneToOneField('Price')
    
class Features(models.Model):
    furnished = models.BooleanField(default=False)
    furniture = models.TextField(blank=True)

class Price(models.Model):
    monthly_rent = models.IntegerField()
    prorated = models.BooleanField(default=True)
    security_deposit = models.IntegerField()

class Utilities(models.Model):
    water = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
    air_cond = models.IntegerField(default=0)
    heat = models.IntegerField(default=0)
    gas = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)
    cable = models.IntegerField(default=0)
    insurance = models.IntegerField(default=0)
     
class Prohibitions(models.Model):
    can_smoke = models.BooleanField(default=False)
    can_party = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    
