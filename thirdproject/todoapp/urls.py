from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("/", views.index, name="index"),
    path("", views.list_view, name="list_view"),
]
