# Generated by Django 4.2.5 on 2023-11-04 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0029_alter_userprofile_account_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account_expiry',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 3, 20, 29, 32, 483199)),
        ),
    ]
