# Generated by Django 4.0.5 on 2022-07-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_account_address_account_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='mobile_no',
            field=models.IntegerField(),
        ),
    ]