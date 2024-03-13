from django.urls import path

from timetracker import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start_task/", views.start_task, name="start_task"),
    path("end_task/", views.end_task, name="end_task"),
]
