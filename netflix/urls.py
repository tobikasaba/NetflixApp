from django.urls import path
from .import views

app_name="netflix"

urlpatterns = [
    path("", views.index, name="index"),
    # views.index is a reference to views.py
    path("<int:netflix_id>", views.detail, name="detail")
]
