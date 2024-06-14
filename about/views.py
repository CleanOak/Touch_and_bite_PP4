from django.shortcuts import render
from .models import About, Contact

# Create your views here.

def about_us(request):
    about_info = About.objects.all()
    contact_info = Contact.objects.all()
    return render(request, 'about/about.html', {'about_info': about_info, 'contact_info': contact_info})
