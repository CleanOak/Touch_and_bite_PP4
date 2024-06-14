from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'requested_date', 'requested_time', 'number_of_people']