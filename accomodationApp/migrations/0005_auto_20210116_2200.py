# Generated by Django 3.1.5 on 2021-01-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodationApp', '0004_auto_20210116_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='note',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewText',
            field=models.CharField(blank=True, max_length=1023),
        ),
    ]
