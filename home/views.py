from django.shortcuts import render


# Create your views here.


def home(request):
    """
    A view to display the home page
    """
    return render(request, 'home/index.html')
