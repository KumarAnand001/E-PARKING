# Generated by Django 3.0.5 on 2020-06-24 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkingplaces',
            old_name='Name',
            new_name='parkplace',
        ),
    ]
