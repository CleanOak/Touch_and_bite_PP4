# Generated by Django 4.2.13 on 2024-06-13 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='food_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]