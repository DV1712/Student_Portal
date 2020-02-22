from django.urls import path
from Users import views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path("registration/", views.registration_page, name="Reg Page"),
    path("login/", views.login_page, name="Login Page"),
    path("", views.home, name="Home Page"),
]
