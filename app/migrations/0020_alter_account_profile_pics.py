# Generated by Django 4.0.5 on 2022-07-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_account_experience_account_ratings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pics',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
