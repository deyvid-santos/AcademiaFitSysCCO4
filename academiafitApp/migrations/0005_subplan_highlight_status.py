# Generated by Django 3.2.9 on 2021-11-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0004_subplan_subplanfeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='highlight_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
