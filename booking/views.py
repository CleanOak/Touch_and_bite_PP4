from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
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


class BookingList(generic.ListView):
    """
    This view will display all the bookings
    a particular user has made
    """
    model = Booking
    queryset = Booking.objects.filter().order_by('-requested_date')
    template_name = 'booking_list.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):

        booking = Booking.objects.all()
        paginator = Paginator(Booking.objects.filter(user=request.user), 4)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)
        today = datetime.datetime.now().date()

        for date in booking:
            if date.requested_date < today:
                date.status = 'Booking Expired'

        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
            return render(
                request,
                'booking/booking_list.html',
                {
                    'booking': booking,
                    'bookings': bookings,
                    'booking_page': booking_page})
        else:
            return redirect('accounts/login.html')

class EditBooking(SuccessMessageMixin, UpdateView):
    """
    This view will display the booking by it's primary key
    so the user can then edit it
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/edit_booking.html'
    success_message = 'Booking has been updated.'

    def get_success_url(self, **kwargs):
        return reverse('booking_list')

def cancel_booking(request, pk):
    """
    Deletes the booking identified by it's primary key by the user
    """
    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('booking_list')

    return render(
        request, 'booking/cancel_booking.html', {'booking': booking})

