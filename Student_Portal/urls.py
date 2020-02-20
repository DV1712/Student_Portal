from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from Users import views as user_views  #this one is for default login page only
from Profile import views as profile_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', user_views.register, name="Reg Page"),
    path('profile/', profile_views.reg_user, name="Profile Page"),
    path("", include("Users.urls")),


]
