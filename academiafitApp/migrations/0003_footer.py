# Generated by Django 3.2.9 on 2021-11-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0002_auto_20211114_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
    ]
