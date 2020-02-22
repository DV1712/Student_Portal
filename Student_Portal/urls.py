from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from Users import views as user_views  #this one is for default login page only


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', user_views.register, name="Reg Page"),
    path('profile/', include("Profile.urls")),
    path("", include("Users.urls")),


]
