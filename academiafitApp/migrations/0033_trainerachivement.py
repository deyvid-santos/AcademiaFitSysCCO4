# Generated by Django 3.2.9 on 2021-11-17 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0032_subscription_reg_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerAchivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='trainer_achivements/')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer')),
            ],
        ),
    ]
