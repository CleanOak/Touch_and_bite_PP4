from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact


class ContactForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))

    
    # phone = PhoneNumberField(widget=forms.TextInput(
    #     attrs={'placeholder': ('+44792002022')}
    # ))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']