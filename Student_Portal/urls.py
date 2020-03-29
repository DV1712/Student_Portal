from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from Users import views
import Users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include("Profile.urls")),
    path("", include("Users.urls")),

]
