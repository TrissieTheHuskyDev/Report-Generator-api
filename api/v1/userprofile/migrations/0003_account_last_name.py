# Generated by Django 3.0.8 on 2020-07-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_account_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default=' ', max_length=30),
        ),
    ]
