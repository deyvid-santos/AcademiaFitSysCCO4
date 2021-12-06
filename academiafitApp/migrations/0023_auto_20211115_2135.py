# Generated by Django 3.2.9 on 2021-11-16 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0022_rename_subs_cliente_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='trainers/')),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='img',
            field=models.ImageField(null=True, upload_to='subs/'),
        ),
    ]
