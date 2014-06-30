from django.db import models

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip_code = models.IntegerField()
    neightborhood = models.CharField(max_length=50)
