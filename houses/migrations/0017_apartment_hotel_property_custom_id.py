# Generated by Django 5.2.1 on 2025-06-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0016_alter_property_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('houses.property',),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
            ],
            options={
                'verbose_name': 'Гостиница',
                'verbose_name_plural': 'Гостиницы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('houses.property',),
        ),
        migrations.AddField(
            model_name='property',
            name='custom_id',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
