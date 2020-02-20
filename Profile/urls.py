from django.urls import path
from Users import views
from Profile import templates
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # path("", views.reg_user, name="Profile Page"),
]