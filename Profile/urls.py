from django.urls import path
from Profile import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from Student_Portal import settings

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path("edit/", views.edit_user, name="Edit Page"),
    path("browse/", views.browse_page, name="Browse Page"),
    path("attendance/", views.attendance, name="Attendance Page"),
    path(r'<sap>/', views.show_user, name="Profile Page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
