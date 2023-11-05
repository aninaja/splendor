# Generated by Django 4.2.5 on 2023-11-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_is_code_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_code_used',
        ),
        migrations.AddField(
            model_name='transaction',
            name='dicounted_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
