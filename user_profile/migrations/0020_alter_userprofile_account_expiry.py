# Generated by Django 4.2.5 on 2023-11-02 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0019_alter_userprofile_account_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account_expiry',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 1, 15, 0, 37, 280071)),
        ),
    ]
