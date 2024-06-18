from django.urls import path
from . import views

urlpatterns = [
    path('', views.Reservations.as_view(), name='booking'),
    path('confirmation', views.Confirmed.as_view(), name='confirmation'),
    path('booking_list', views.BookingList.as_view(), name='booking_list'),
    path('edit_booking/<int:pk>',
         views.EditBooking.as_view(), name='edit_booking'),
    path('cancel_booking/<int:pk>',
         views.cancel_booking, name='cancel_booking'),
]