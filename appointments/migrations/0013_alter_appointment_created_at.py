# Generated by Django 4.2.5 on 2023-11-23 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0012_alter_appointment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 5, 16, 29, 220568)),
        ),
    ]
