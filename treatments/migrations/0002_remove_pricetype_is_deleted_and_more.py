# Generated by Django 4.2.5 on 2023-10-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricetype',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='service',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='treatmentarea',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='pricetype',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='treatmentarea',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
