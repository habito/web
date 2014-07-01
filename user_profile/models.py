from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.IntegerField(max_length=1, default=1)
    start_date = models.DateField(_(Date), default=datetime.date.today)    

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
