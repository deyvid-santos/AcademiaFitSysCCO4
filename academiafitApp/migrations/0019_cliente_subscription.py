# Generated by Django 3.2.9 on 2021-11-15 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academiafitApp', '0018_alter_subplan_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.CharField(max_length=50)),
                ('plano', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.subplan')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=20)),
                ('endereco', models.TextField()),
                ('img', models.ImageField(upload_to='subs/')),
                ('subs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cliente',
            },
        ),
    ]