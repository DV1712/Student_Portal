from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True)


# class Student(User):
#     pass
#     sap_id = models.IntegerField(default=0, unique=True)
#     s_course = models.CharField(max_length=10, default='B.TECH')
#     s_stream = models.CharField(max_length=50, default="CS")
#
#
# class Faculty(User):
#     f_department = models.CharField(max_length=50, default="Computer")
