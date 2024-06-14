from django.db import models

# Create your models here.


FOOD_TYPES = ((0, 'Starters'), (1, 'Mains'), (2, 'Desserts'), (3, 'New'))

class FoodItem(models.Model):
    """
    A class for food items model, which includes
    types of food services
    """
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(
        max_length= 50,
        unique=True
    )
    description = models.CharField(
        max_length=200,
        unique=True
    )
    price = models.FloatField()
    food_type = models.IntegerField(
        choices=FOOD_TYPES,
        default=3
    )
    food_image = models.ImageField(upload_to='images', blank=True, null=True)
    available = models.BooleanField(default=True)


    class Meta:
        ordering = ['-food_type']

    def __str__(self):
        return self.food_name
