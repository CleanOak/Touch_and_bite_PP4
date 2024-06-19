from . import views
from django.urls import path


urlpatterns = [
    path('', views.about_us, name='about'),
    # path('contact_success', views.ContactService.as_view(), name='contact_success'),
]