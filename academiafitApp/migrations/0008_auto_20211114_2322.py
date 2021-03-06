# Generated by Django 3.2.9 on 2021-11-15 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academiafitApp', '0007_alter_banners_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name': 'Banners do site'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Perguntas frequentes'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Rodapé do site'},
        ),
        migrations.AlterModelOptions(
            name='formulario',
            options={'verbose_name': 'Formulário'},
        ),
        migrations.AlterModelOptions(
            name='galeria',
            options={'verbose_name': 'Galerias'},
        ),
        migrations.AlterModelOptions(
            name='galeriafotos',
            options={'verbose_name': 'Galeria (Fotos)'},
        ),
        migrations.AlterModelOptions(
            name='pagina',
            options={'verbose_name': 'Páginas editáveis'},
        ),
        migrations.AlterModelOptions(
            name='plandiscount',
            options={'verbose_name': 'Descontos dos planos'},
        ),
        migrations.AlterModelOptions(
            name='servicos',
            options={'verbose_name': 'Serviços do site'},
        ),
        migrations.AlterModelOptions(
            name='subplan',
            options={'verbose_name': 'Planos do site'},
        ),
        migrations.AlterModelOptions(
            name='subplanfeature',
            options={'verbose_name': 'Detalhes do plano do site'},
        ),
    ]
