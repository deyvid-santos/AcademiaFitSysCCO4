# Generated by Django 3.2.9 on 2021-11-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0033_trainerachivement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerachivement',
            name='img',
            field=models.ImageField(null=True, upload_to='trainer_achivements/'),
        ),
    ]
