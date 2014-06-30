from django.db import models

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
