from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.

status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Booking Rejected', 'Booking Rejected'),
    ('Booking Expired', 'Booking Expired'),
)


class Service(models.Model):
    """
    a class for the Service model
    """
    event_name = models.CharField(max_length=100)


    class Meta:
        
        ordering = ['-event_name']

    def __str__(self):
        
        return self.event_name


# The booking model for the database

class Booking(models.Model):
    """
    a class for the Booking model
    """
    # booking_id = models.AutoField(primary_key=True, default=1)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=True)
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='awaiting confirmation'
        )
    email = models.EmailField(max_length=254, default="")
    requested_date = models.DateField()
    requested_time = models.TimeField()
    number_of_people = models.IntegerField()

    class Meta:
        ordering = ['-requested_time']
        unique_together = ('requested_date', 'requested_time', 'service')

    def __str__(self):
        return f'booked by {self.user} on {self.requested_date} at {self.requested_time}'