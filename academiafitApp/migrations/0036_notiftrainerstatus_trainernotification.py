# Generated by Django 3.2.9 on 2021-11-22 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0035_auto_20211117_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NotifTrainerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainernotification')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer')),
            ],
            options={
                'verbose_name_plural': 'Estado da notificação do treinador',
            },
        ),
    ]