# Generated by Django 3.2.9 on 2021-11-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0005_subplan_highlight_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_mes', models.IntegerField()),
                ('total_desconto', models.IntegerField()),
            ],
        ),
    ]
