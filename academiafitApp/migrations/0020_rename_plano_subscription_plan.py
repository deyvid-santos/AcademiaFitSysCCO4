# Generated by Django 3.2.9 on 2021-11-15 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0019_cliente_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='plano',
            new_name='plan',
        ),
    ]
