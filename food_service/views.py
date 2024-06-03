from django.shortcuts import render
from .models import FoodItem

# Create your views here.
def food_menu(request):
    food_list = FoodItem.objects.all()
    return render( request, 'food_service/food_service.html', {'food_list': food_list})