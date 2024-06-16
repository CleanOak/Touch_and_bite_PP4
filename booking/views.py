from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Service, Booking
from .forms import BookingForm


# Create your views here.
def create_booking(request):
    bookings = Booking.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Success')
    else:
        form = BookingForm()
    
    return render(request, 'booking/booking.html', {'bookings': bookings})






# def service_list(request):
#     services = Service.objects.all()
#     return render(request, 'booking/service_list.html', {'services':services} )

# @login_required
# # def create_booking(request, service_id):
#     # service = Service.objects.get(id=service_id)
# if request.method == 'POST':
#     form = BookingForm(request.POST)
#     if form.is_valid():
#         booking = form.save(commit=False)
#         booking.user = request.user
#         booking.service = service
#         booking.save()
#         return redirect('booking_list')
# else:
#     form = BookingForm(initial={'service': service})
# return render(request, 'booking/booking.html', {'form': form, 'service': service})


# @login_required
# def booking_list(request):
#     bookings = Booking.objects.filter(user=request.user)
#     return render(request, 'booking/booking_list.html', {'booking': booking})


