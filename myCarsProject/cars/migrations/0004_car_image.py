# Generated by Django 5.1.7 on 2025-04-26 08:50

import cars.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cars.models.car_image_path, verbose_name='Изображение'),
        ),
    ]
