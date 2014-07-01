from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.IntegerField()
    start_date = models.DateField(default=datetime.date.today)    
    	
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
