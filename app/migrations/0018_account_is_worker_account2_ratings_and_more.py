# Generated by Django 4.0.5 on 2022-07-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_account2'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_worker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account2',
            name='ratings',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account2',
            name='experience',
            field=models.BigIntegerField(default=0),
        ),
    ]
