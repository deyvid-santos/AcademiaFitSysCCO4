# Generated by Django 3.2.9 on 2021-11-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0015_auto_20211115_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='validity_days',
            field=models.IntegerField(null=True),
        ),
    ]
