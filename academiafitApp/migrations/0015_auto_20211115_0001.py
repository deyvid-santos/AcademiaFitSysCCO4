# Generated by Django 3.2.9 on 2021-11-15 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0014_plandiscount_subplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plandiscount',
            old_name='total_desconto',
            new_name='total_discount',
        ),
        migrations.RenameField(
            model_name='plandiscount',
            old_name='total_mes',
            new_name='total_months',
        ),
    ]
