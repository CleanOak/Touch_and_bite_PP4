from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Event(models.Model):
    """
    A class for the About model
    """
    event_type = models.CharField(max_length=200)
    event_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return str(self.event_type) if self.event_type else ''