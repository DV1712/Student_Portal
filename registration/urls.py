from django.urls import path
from registration import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registration/<name>", views.hello_there, name="hello_there"),
]

