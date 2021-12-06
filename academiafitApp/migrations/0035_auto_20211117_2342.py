# Generated by Django 3.2.9 on 2021-11-18 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0034_alter_trainerachivement_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.CreateModel(
            name='TrainerSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.IntegerField()),
                ('amt_date', models.DateField()),
                ('remark', models.TextField(blank=True)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer')),
            ],
            options={
                'verbose_name_plural': 'Salário do Treinador',
            },
        ),
    ]