# Generated by Django 3.2.9 on 2021-12-06 02:03

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academiafitApp', '0042_alter_servicospaginas_servicopagina'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appsetting',
            options={'verbose_name_plural': 'Logomarca'},
        ),
        migrations.AlterModelOptions(
            name='assignsubscriber',
            options={'verbose_name_plural': 'Treinador do Cliente'},
        ),
        migrations.AlterModelOptions(
            name='notifuserstatus',
            options={'verbose_name_plural': 'Notificação Usuário'},
        ),
        migrations.AlterModelOptions(
            name='notify',
            options={'verbose_name_plural': 'Notificação'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name_plural': 'Subscrição'},
        ),
        migrations.AlterModelOptions(
            name='trainer',
            options={'verbose_name_plural': 'Treinador'},
        ),
        migrations.AlterModelOptions(
            name='trainerachivement',
            options={'verbose_name_plural': 'Conquistas do Treinador'},
        ),
        migrations.AlterModelOptions(
            name='trainernotification',
            options={'verbose_name_plural': 'Notificações do Treinador'},
        ),
        migrations.AlterModelOptions(
            name='trainersubscriberreport',
            options={'verbose_name_plural': 'Denúncias'},
        ),
        migrations.AddField(
            model_name='servicos',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Conteúdo da página'),
        ),
        migrations.AlterField(
            model_name='appsetting',
            name='logo_img',
            field=models.ImageField(upload_to='app_logos/', verbose_name='Logomarca'),
        ),
        migrations.AlterField(
            model_name='assignsubscriber',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer', verbose_name='Treinador'),
        ),
        migrations.AlterField(
            model_name='assignsubscriber',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='descricao',
            field=models.CharField(max_length=150, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='img',
            field=models.ImageField(upload_to='banners/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pergunta',
            field=models.CharField(max_length=200, verbose_name='Pergunta'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='resposta',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Resposta'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='detalhes',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Detalhes'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='nome_completo',
            field=models.CharField(max_length=150, verbose_name='Nome completo'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='tempo_envio',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tempo do Envio'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='descricao',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='img',
            field=models.ImageField(null=True, upload_to='galeria/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='titulo',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='galeriafotos',
            name='descricao',
            field=models.CharField(max_length=150, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='galeriafotos',
            name='galeria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.galeria', verbose_name='Galeria'),
        ),
        migrations.AlterField(
            model_name='galeriafotos',
            name='img',
            field=models.ImageField(null=True, upload_to='galeria_imgs/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='notiftrainerstatus',
            name='notif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainernotification', verbose_name='Notificação'),
        ),
        migrations.AlterField(
            model_name='notiftrainerstatus',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='notiftrainerstatus',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer', verbose_name='Treinador'),
        ),
        migrations.AlterField(
            model_name='notifuserstatus',
            name='notif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.notify', verbose_name='Notificação'),
        ),
        migrations.AlterField(
            model_name='notifuserstatus',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='notifuserstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='notify',
            name='notify_detail',
            field=models.TextField(verbose_name='Descrição da notificação'),
        ),
        migrations.AlterField(
            model_name='notify',
            name='read_by_trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer', verbose_name='Lido pelo treinador'),
        ),
        migrations.AlterField(
            model_name='notify',
            name='read_by_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Lido pelo usuário'),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='descricao',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='plandiscount',
            name='total_discount',
            field=models.IntegerField(verbose_name='Desconto'),
        ),
        migrations.AlterField(
            model_name='plandiscount',
            name='total_months',
            field=models.IntegerField(verbose_name='Meses'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='descricao',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='img',
            field=models.ImageField(null=True, upload_to='servicos/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='titulo',
            field=models.CharField(max_length=30, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='servicospaginas',
            name='descricao',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servicospaginas',
            name='servicopagina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.servicos', verbose_name='Serviço'),
        ),
        migrations.AlterField(
            model_name='subplan',
            name='highlight_status',
            field=models.BooleanField(default=False, null=True, verbose_name='Destaque'),
        ),
        migrations.AlterField(
            model_name='subplan',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='subplan',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='subplan',
            name='validity_days',
            field=models.IntegerField(null=True, verbose_name='Validade'),
        ),
        migrations.AlterField(
            model_name='subplanfeature',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='celular',
            field=models.CharField(max_length=20, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='endereco',
            field=models.TextField(verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='img',
            field=models.ImageField(null=True, upload_to='subs/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.subplan', verbose_name='Plano'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.CharField(max_length=50, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='address',
            field=models.TextField(verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='detail',
            field=models.TextField(verbose_name='Detalhes'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='Nome completo'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='img',
            field=models.ImageField(upload_to='trainers/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='mobile',
            field=models.CharField(max_length=100, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Salário'),
        ),
        migrations.AlterField(
            model_name='trainerachivement',
            name='detail',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='trainerachivement',
            name='img',
            field=models.ImageField(null=True, upload_to='trainer_achivements/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='trainerachivement',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='trainerachivement',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer', verbose_name='Treinador'),
        ),
        migrations.AlterField(
            model_name='trainermsg',
            name='message',
            field=models.TextField(verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='trainermsg',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer', verbose_name='Treinador'),
        ),
        migrations.AlterField(
            model_name='trainermsg',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='trainernotification',
            name='notif_msg',
            field=models.TextField(verbose_name='Mensagem de Notificação'),
        ),
        migrations.AlterField(
            model_name='trainersalary',
            name='amt',
            field=models.IntegerField(verbose_name='Montante'),
        ),
        migrations.AlterField(
            model_name='trainersalary',
            name='amt_date',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='trainersalary',
            name='remark',
            field=models.TextField(blank=True, verbose_name='Marcação'),
        ),
        migrations.AlterField(
            model_name='trainersalary',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academiafitApp.trainer', verbose_name='Treinador'),
        ),
        migrations.AlterField(
            model_name='trainersubscriberreport',
            name='report_for_trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_for_trainer', to='academiafitApp.trainer', verbose_name='Denúncia Treinador'),
        ),
        migrations.AlterField(
            model_name='trainersubscriberreport',
            name='report_for_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_for_user', to=settings.AUTH_USER_MODEL, verbose_name='Denúncia Usuário'),
        ),
        migrations.AlterField(
            model_name='trainersubscriberreport',
            name='report_from_trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_from_trainer', to='academiafitApp.trainer', verbose_name='Feito(a) pelo treinador(a)'),
        ),
        migrations.AlterField(
            model_name='trainersubscriberreport',
            name='report_from_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_from_user', to=settings.AUTH_USER_MODEL, verbose_name='Feito pelo usuário'),
        ),
        migrations.AlterField(
            model_name='trainersubscriberreport',
            name='report_msg',
            field=models.TextField(verbose_name='Mensagem de denúncia'),
        ),
    ]
