# Generated by Django 2.2.12 on 2020-04-14 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20200307_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Created'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 4, 14, 19, 38, 59, 150608, tzinfo=utc), verbose_name='Date Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='address_type',
            field=models.CharField(choices=[(1, 'OFFICE'), (2, 'HOME')], default=2, max_length=1),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address_type',
            field=models.CharField(choices=[(1, 'OFFICE'), (2, 'HOME')], default=2, max_length=1),
        ),
    ]