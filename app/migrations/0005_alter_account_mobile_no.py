# Generated by Django 4.0.5 on 2022-07-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_account_address_alter_account_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='mobile_no',
            field=models.CharField(default=' ', max_length=11),
        ),
    ]