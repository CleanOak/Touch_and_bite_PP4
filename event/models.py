from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Event(models.Model):
    """
    A class for the About model
    """
    event_type = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images')
    content = models.TextField()

    def __str__(self):
        return self.event_type