from django.urls import path
from . import views

urlpatterns =[
    # 1 ,2
    path('fullname/',views.fullname),
    # 3
    # path('name/<str:first>/<str:last>/',views.fullname),   
]