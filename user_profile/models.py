from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='../media/profile_images', default='../media/profile_images/pp.png')
    phone_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    annual_pay = models.IntegerField()
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
