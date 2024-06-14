from django.shortcuts import render
from .models import Event


def event_page(request):
    event_list = Event.objects.all()
    return render(request, 'event/event.html', {'event_list': event_list})