# Generated by Django 5.2.1 on 2025-05-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_remove_property_apartment_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='property',
            name='longitude',
        ),
    ]
