# Generated by Django 3.2.9 on 2021-11-15 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0021_rename_preco_subscription_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='subs',
            new_name='user',
        ),
    ]
