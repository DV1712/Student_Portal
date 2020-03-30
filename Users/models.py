from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)