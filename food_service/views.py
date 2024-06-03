from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def food_menu(request):
    return HttpResponse("Hello Touch and Bite")