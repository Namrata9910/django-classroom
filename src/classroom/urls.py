from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("assignment/<str:code>", views.assignmentPage, name="assignment"),
]
