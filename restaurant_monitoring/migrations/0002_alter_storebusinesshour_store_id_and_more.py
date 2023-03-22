# Generated by Django 4.1.4 on 2023-03-22 18:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storebusinesshour',
            name='store_id',
            field=models.TextField(default=uuid.UUID('65eb5e72-e6e2-4b48-bf83-07faf2da6be3')),
        ),
        migrations.AlterField(
            model_name='storemenuhour',
            name='store_id',
            field=models.TextField(default=uuid.UUID('f66d89c0-796f-45c1-b457-5d860a265932')),
        ),
    ]