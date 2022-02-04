from django.urls import path
from . import views

urlpatterns = [
    path("", views.qualifications, name="Qualifications"),
]