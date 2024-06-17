from django.urls import path
from . import views

urlpatterns = [
    # path('book/<int:service_id>/', views.create_booking, name='create_booking'),
    # path('', views.booking_list, name='booking_list'),
    path('', views.Reservations.as_view(), name='booking'),
    path('confirmation', views.Confirmed.as_view(), name='confirmation'),
]