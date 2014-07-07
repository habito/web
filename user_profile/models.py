from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='../media/profile_images', default='../media/profile_images/pp.png')
    phone_number = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    annual_pay = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
