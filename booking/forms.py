from django import forms
from crispy_forms.helper import FormHelper
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking

class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    requested_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()} 
        )
    )

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+44792002022')}
    ))

    class Meta:
        model = Booking
        fields = ['service', 'requested_date', 'requested_time', 'number_of_people', 'phone', 'email']

    

    