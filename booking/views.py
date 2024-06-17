from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator

from .models import Service, Booking
from .forms import BookingForm


# This will get the user information if they are logged in

def get_user_instance(request):
    """
    retrieves user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class Reservations(generic.ListView):
    success_messgae = 'Booking has been made.'

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'booking/booking.html', {'booking_form': booking_form})


    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database
        """
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request, "Booking succesful, awaiting confirmation")
            return render(request, 'booking/confirmation.html')

        return render(request, 'booking/booking.html',
                      {'booking_form': booking_form})



class Confirmed(generic.DetailView):
    """
    This view will display confirmation on a successful booking
    """
    template_name = 'booking/confirmation.html'

    def get(self, request):
        return render(request, 'booking/confirmation.html')


