from django.contrib.auth.models import User
from django.db import models


class Farmer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    nationality = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
