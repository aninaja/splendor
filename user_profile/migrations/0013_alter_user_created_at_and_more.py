# Generated by Django 4.2.5 on 2023-11-01 09:37

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_alter_user_created_at_alter_user_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='account_expiry',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 31, 9, 37, 21, 890661)),
        ),
    ]
