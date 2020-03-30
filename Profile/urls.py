from django.urls import path
from Profile import views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path("edit/", views.edit_user, name="Edit Page"),
    path("browse/", views.browse_page, name="Browse Page"),
    path(r'<sap>/', views.show_user, name="Profile Page")
]
