from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_view, name="index"),
    path("list/", views.list_view, name="list"),
    path("<id>", views.detail_view, name="detail"),
    path("<id>/update", views.update_view, name="update_view"),
]
