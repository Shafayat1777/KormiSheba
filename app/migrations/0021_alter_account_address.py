# Generated by Django 4.0.5 on 2022-08-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_account_profile_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
