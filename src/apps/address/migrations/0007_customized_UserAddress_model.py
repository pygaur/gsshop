# Generated by Django 3.0.9 on 2020-08-11 20:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_auto_20181115_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='address_type',
            field=models.CharField(choices=[('1', 'OFFICE'), ('2', 'HOME')], default='2', max_length=1),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='alt_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Alternate Contact Number', max_length=128, region=None, verbose_name='Alternate Phone number'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='email',
            field=models.EmailField(blank=True, help_text='Email Address', max_length=254, verbose_name='Email ID'),
        ),
    ]
