# Generated by Django 4.0.5 on 2022-07-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
    ]