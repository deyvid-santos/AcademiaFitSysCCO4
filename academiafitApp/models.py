from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.forms.widgets import PasswordInput
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import json

# Banners
class Banners(models.Model):
    img=models.ImageField(upload_to="banners/",verbose_name='Imagem')
    descricao=models.CharField(max_length=150,verbose_name='Descrição')
    
    # Retorna a descrição (um título do objeto)
    def __str__(self):
        return self.descricao
    
    # Retorna um marcador de imagem HTML
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Banners do site"
    

# Servicos
class Servicos(models.Model):
    titulo=models.CharField(max_length=30,verbose_name='Título')
    descricao=RichTextField(blank=True,null=True,verbose_name='Descrição')
    img=models.ImageField(upload_to="servicos/", null=True,verbose_name='Imagem')
    body=RichTextUploadingField(blank=True,null=True,verbose_name='Conteúdo da página')
    
    # Retorna o titulo (um título do objeto)
    def __str__(self):
        return self.titulo
    
    # Retorna um marcador de imagem HTML
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Serviços do site"
        

    # Páginas
class Pagina(models.Model):
    titulo=models.CharField(max_length=200,verbose_name='Título')
    descricao=RichTextUploadingField(null=True,verbose_name='Descrição')
    
    # Retorna o titulo (um titulo do objeto)
    def __str__(self):
        return self.titulo
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Páginas editáveis"
        
        
# Faqs (Perguntas frequentes)
class Faq(models.Model):
    pergunta=models.CharField(max_length=200,verbose_name='Pergunta')
    resposta=RichTextField(blank=True,null=True,verbose_name='Resposta')
    
    # Retorna a pergunta (um titulo do objeto)
    def __str__(self):
        return self.pergunta
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Perguntas frequentes"
        
# Formulário
class Formulario(models.Model):
    nome_completo=models.CharField(max_length=150,verbose_name='Nome completo')
    email=models.EmailField(max_length=255,verbose_name='E-mail')
    detalhes=RichTextField(blank=True,null=True,verbose_name='Detalhes')
    tempo_envio=models.DateTimeField(auto_now_add=True,verbose_name='Tempo do Envio')
    
    # Retorna o nome completo (um titulo do objeto)
    def __str__(self):
        return self.nome_completo
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Formulário"
        
        
# Galeria (Grupo)
class Galeria(models.Model):
    titulo=models.CharField(max_length=150,verbose_name='Título')
    descricao=RichTextField(blank=True,null=True,verbose_name='Descrição')
    img=models.ImageField(upload_to="galeria/",null=True,verbose_name='Imagem') #Thumbnail da Galeria
    
    # Retorna o titulo (um titulo do objeto)
    def __str__(self):
        return self.titulo
    
    # Retorna um marcador de imagem html
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Galerias"
        
        
# Galeria (Imagens do grupo)
class GaleriaFotos(models.Model):
    galeria=models.ForeignKey(Galeria, on_delete=models.CASCADE,null=True,verbose_name='Galeria')
    descricao=models.CharField(max_length=150,verbose_name='Descrição')
    img=models.ImageField(upload_to="galeria_imgs/",null=True,verbose_name='Imagem')
    
    # Retorna a descricao (um titulo do objeto)
    def __str__(self):
        return self.descricao
    
    # Retorna um marcador de imagem html
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
 
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Galeria (Fotos)"

# Footer
class Footer(models.Model):
    descricao=models.CharField(max_length=200,verbose_name='Descrição')
    
    def __str__(self):
        return self.descricao
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Rodapé do site"
# Plano
class SubPlan(models.Model):
    title=models.CharField(max_length=150,verbose_name='Título')
    price=models.IntegerField(null=True,verbose_name='Preço')
    highlight_status=models.BooleanField(default=False,null=True,verbose_name='Destaque') 
    validity_days=models.IntegerField(null=True,verbose_name='Validade')
    
    def __str__(self):
        return self.title
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Planos do site"
    
# Plano Features
class SubPlanFeature(models.Model):
    subplan=models.ManyToManyField(SubPlan)
    title=models.CharField(max_length=150,verbose_name='Título')
    
    def __str__(self):
        return self.title
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Detalhes (Planos)"
    
# Descontos
class PlanDiscount(models.Model):
    subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True, verbose_name='Plano')
    total_months=models.IntegerField(verbose_name='Meses')
    total_discount=models.IntegerField(verbose_name='Desconto')
    
    def __str__(self):
        return str(self.total_mes)
    
    # Altera o nome do Label
    class Meta:
        verbose_name_plural = "Descontos (Planos)"
        
        
# Clientes
class Subscriber(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,verbose_name='Usuário')
    celular=models.CharField(max_length=20,verbose_name='Celular')
    endereco=models.TextField(verbose_name='Endereço')
    img=models.ImageField(upload_to="subs/",null=True,verbose_name='Imagem')

    def __str__(self):
        return str(self.user)
    
    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' % self.img.url)
        else:
            return 'no-image'
    
    @receiver(post_save,sender=User)
    def create_subscriber(sender,instance,created,**kwrags):
	    if created:
             Subscriber.objects.create(user=instance)
          
    class Meta:
        verbose_name_plural = "Cliente"

# Subscrição
class Subscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,verbose_name='Usuário')
    plan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True,verbose_name='Plano')
    price=models.CharField(max_length=50,verbose_name='Preço')

    reg_date=models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        verbose_name_plural = "Subscrição"

# Treinador
class Trainer(models.Model):
    full_name=models.CharField(max_length=100,verbose_name='Nome completo')
    username=models.CharField(max_length=100,null=True, verbose_name='Usuário')
    pwd=models.CharField(max_length=50,null=True, verbose_name='Senha')
    mobile=models.CharField(max_length=100, verbose_name='Celular')
    address=models.TextField(verbose_name='Endereço')
    is_active=models.BooleanField(default=False,verbose_name='Ativo')
    detail=models.TextField(verbose_name='Detalhes')
    img=models.ImageField(upload_to="trainers/",verbose_name='Imagem')
    salary=models.DecimalField(max_digits=6,decimal_places=2,default=0,verbose_name='Salário')


    def __str__(self):
        return str(self.full_name)

    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' % (self.img.url))
        else:
            return 'no-image'
        
    class Meta:
        verbose_name_plural = "Treinador"


# Notificação
class Notify(models.Model):
    notify_detail=models.TextField(verbose_name='Descrição da notificação')
    read_by_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,verbose_name='Lido pelo usuário')
    read_by_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Lido pelo treinador')
    
    def __str__(self):
        return str(self.notify_detail)
 
    
    class Meta:
        verbose_name_plural = "Notificação"
        
        
# Marcar a notificação como lida
class NotifUserStatus(models.Model):
    notif=models.ForeignKey(Notify, on_delete=models.CASCADE, verbose_name='Notificação')
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    status=models.BooleanField(default=False,verbose_name='Status')
    
    class Meta:
        verbose_name_plural = "Notificação Usuário"
    
# Relação Cliente para o Treinador
class AssignSubscriber(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, verbose_name='Usuário')
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='Treinador')
    
    def __str__(self):
        return str(self.user)
    

    class Meta:
        verbose_name_plural = "Treinador do Cliente"



# Conquistas do treinador
class TrainerAchivement(models.Model):
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,verbose_name='Treinador')
    title=models.CharField(max_length=100,verbose_name='Título')
    detail=models.TextField(verbose_name='Descrição')
    img=models.ImageField(upload_to="trainer_achivements/",null=True,verbose_name='Imagem')
    
    def __str__(self):
        return str(self.title)
    
    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' % self.img.url)
        else:
            return 'no-image'

    class Meta:
        verbose_name_plural = "Conquistas do Treinador"
# Salário do Treinador
class TrainerSalary(models.Model):        
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,verbose_name='Treinador')
    amt=models.IntegerField(verbose_name='Montante')
    amt_date=models.DateField(verbose_name='Data')
    remark=models.TextField(blank=True,verbose_name='Marcação')
    
    class Meta:
        verbose_name_plural='Salário do Treinador'
        
    def __str__(self):
        return str(self.trainer.full_name)
    
# Notificações do Treinador
class TrainerNotification(models.Model):
    notif_msg=models.TextField(verbose_name='Mensagem de Notificação')
    
    def __str__(self):
        return str(self.notif_msg)
    
    def save(self, *args, **kwargs):
        super(TrainerNotification, self).save(*args,**kwargs)
        channel_layer=get_channel_layer()
        notif=self.notif_msg
        total=TrainerNotification.objects.all().count()
        async_to_sync(channel_layer.group_send)(
            'noti_group_name',{
                'type':'send_notification',
                'value':json.dumps({'notif':notif,'total':total})
            }
        )   


    class Meta:
        verbose_name_plural = "Notificações do Treinador"
    

#Marcar a notificação como lida (treinador)
class NotifTrainerStatus(models.Model):
    notif=models.ForeignKey(TrainerNotification, on_delete=models.CASCADE, verbose_name='Notificação')
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,verbose_name='Treinador')
    status=models.BooleanField(default=False,verbose_name='Status')
    
    class Meta:
        verbose_name_plural='Estado da notificação do treinador'
        

# Mensagem do Subscriber        
class TrainerMsg(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,verbose_name='Usuário')
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,verbose_name='Treinador')
    message=models.TextField(verbose_name='Mensagem')
    
    
    class Meta:
        verbose_name_plural='Mensagens do treinador'
        
        

# Relatórios (Treinador)
class TrainerSubscriberReport(models.Model):
    report_for_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='report_for_trainer',verbose_name='Denúncia Treinador')
    report_for_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='report_for_user',verbose_name='Denúncia Usuário')
    report_from_trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='report_from_trainer',blank=True,verbose_name='Feito(a) pelo treinador(a)')
    report_from_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='report_from_user',blank=True,verbose_name='Feito pelo usuário')
    report_msg=models.TextField(verbose_name='Mensagem de denúncia')
    
    class Meta:
        verbose_name_plural = "Denúncias"

# Configurações de Logo
class AppSetting(models.Model):
    logo_img=models.ImageField(upload_to='app_logos/',verbose_name='Logomarca')

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.logo_img.url))
    
    class Meta:
        verbose_name_plural = 'Logomarca'