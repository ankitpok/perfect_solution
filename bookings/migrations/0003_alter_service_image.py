# Generated by Django 5.0.6 on 2024-07-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_remove_service_category_remove_service_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/service_images'),
        ),
    ]
