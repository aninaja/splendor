# Generated by Django 4.2.5 on 2023-11-17 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_alter_appointment_created_at_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 9, 48, 59, 960490)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(choices=[('---------', '---------'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(12, 0), '12:00 PM'), (datetime.time(13, 0), '1:00 PM'), (datetime.time(14, 0), '2:00 PM'), (datetime.time(15, 0), '3:00 PM'), (datetime.time(16, 0), '4:00 PM'), (datetime.time(17, 0), '5:00 PM'), (datetime.time(18, 0), '6:00 PM'), (datetime.time(19, 0), '7:00 PM'), (datetime.time(20, 0), '8:00 PM')]),
        ),
    ]
