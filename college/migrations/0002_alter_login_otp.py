# Generated by Django 3.2.8 on 2022-07-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='otp',
            field=models.CharField(max_length=15),
        ),
    ]
