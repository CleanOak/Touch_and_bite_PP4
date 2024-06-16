from django.urls import path
from . import views

urlpatterns = [
    # path('', views.service_list, name='service_list'),
    # path('book/<int:service_id>/', views.create_booking, name='create_booking'),
    # path('', views.booking_list, name='booking_list'),
    path('', views.create_booking, name='booking'),
]