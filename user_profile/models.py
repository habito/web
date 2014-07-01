from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name