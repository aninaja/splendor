# Generated by Django 4.2.5 on 2023-11-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_rename_dicounted_amount_transaction_discounted_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='offer_code',
            field=models.CharField(default=None, max_length=50),
        ),
    ]