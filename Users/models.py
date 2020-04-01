from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    user_img = models.URLField()
    languages = models.CharField(max_length=1000)
    projects = models.CharField(max_length=1000)
    cgpa = models.CharField(max_length=4)
    core = models.CharField(max_length=500)
    experience = models.CharField(max_length=500)

    @property
    def get_user_info(self):
        return UserInfo.objects.filter()

    @property
    def get_user(self):
        return User.objects.filter()
