# Generated by Django 3.2.9 on 2021-11-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0024_auto_20211115_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='pwd',
            field=models.CharField(max_length=50, null=True, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='username',
            field=models.CharField(max_length=100, null=True, verbose_name='Usuário'),
        ),
    ]
