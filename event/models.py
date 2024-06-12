from django.db import models

# Create your models here.

class Event(models.Model):
    """
    A class for the About model
    """
    event_type = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title