# Generated by Django 2.2.5 on 2020-09-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='instant_room',
            field=models.BooleanField(default=False),
        ),
    ]
