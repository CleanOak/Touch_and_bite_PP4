from django.urls import path
from . import views

urlpatterns =[
   path('food_service/', views.food_menu, name ='food_service') 
]