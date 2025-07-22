from django.urls import path
from . import views

urlpatterns =[
    path('sum/',views.sum),
    path('fullname/',views.fullname),
    path ('avg/',views.avg),
    path('power/',views.power),
    path('evenNum/',views.evenNum)
]