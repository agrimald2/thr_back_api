# Generated by Django 5.0.2 on 2024-03-11 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihr_api', '0008_billingaccount_payment_amount_dollars_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaccount',
            name='key_1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='billingaccount',
            name='key_2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]