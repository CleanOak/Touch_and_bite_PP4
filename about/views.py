from django.shortcuts import render , redirect, reverse
from .models import About, Contact
from django.views import generic, View
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def about_us(request):
    about_info = About.objects.all()
    contact_form = ContactForm()
    


    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request, "Your Enquiries have been recieved by us!")
            return render(request, 'about/contact_success.html')
    else:
        contact_form = ContactForm()
    
    return render(request, 'about/about.html', {'about_info': about_info, 'contact_form': contact_form})



   

