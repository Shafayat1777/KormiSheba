# Generated by Django 4.0.5 on 2022-07-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_image_account_profile_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pics',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
