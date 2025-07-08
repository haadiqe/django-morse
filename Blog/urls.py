from django.urls import path
from . import views

urlpatterns = [
    path('dateTime/', views.date_time),
]