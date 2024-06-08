from . import views
from django.urls import path


urlpatterns = [
    path('', views.event_page, name='event'),
]