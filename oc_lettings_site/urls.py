from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
    path("profiles/", views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
    path("404/", views.custom_404_view, name="404"),
    path("500/", views.custom_500_view, name="500"),
    path("admin/", admin.site.urls),
]
