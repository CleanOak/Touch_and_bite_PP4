from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']