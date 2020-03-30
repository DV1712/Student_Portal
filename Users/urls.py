from django.urls import path
from Users import views
from django.views.generic.base import RedirectView
from django.conf.urls import url
from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    path("registration/", views.registration_page, name="Reg Page"),
    path("login/", views.login_page, name="Login Page"),
    path("logout", views.logout, name="logout"),
    # -----v----- django default reg page -----v-----
    path("", views.home, name="Home Page"),
]
