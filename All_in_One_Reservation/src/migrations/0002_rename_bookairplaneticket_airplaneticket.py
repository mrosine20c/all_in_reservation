# Generated by Django 4.1.7 on 2023-03-16 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookAirPlaneTicket',
            new_name='AirPlaneTicket',
        ),
    ]