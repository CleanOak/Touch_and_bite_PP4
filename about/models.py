from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    """
    A class for the About model
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    about_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    A class for the contact model
    """
    message_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,on_delete=models.CASCADE,
        related_name="contact_user",
        null=True
        )
    name = models.CharField(
        max_length=50,
        null = True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    phone = PhoneNumberField(null=True)
    message = models.TextField()

    class Meta:
        ordering = ['created_date']

    
    def __str__(self):
        return self.name

