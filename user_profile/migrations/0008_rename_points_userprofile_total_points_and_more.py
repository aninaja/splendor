# Generated by Django 4.2.5 on 2023-11-01 01:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_userprofile_account_expiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='points',
            new_name='total_points',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='account_expiry',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 31, 1, 34, 9, 925725)),
        ),
    ]
