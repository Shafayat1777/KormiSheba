# Generated by Django 4.0.5 on 2022-07-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_account_mobile_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='mobile_no',
        ),
        migrations.AddField(
            model_name='account',
            name='mobile_number',
            field=models.CharField(default='', max_length=11),
        ),
    ]