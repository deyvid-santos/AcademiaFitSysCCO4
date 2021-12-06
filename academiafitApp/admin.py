from django.contrib import admin
from academiafitApp import models

# Registra o que mostra na aba de administracao

## Administração dos Banners
class BannerAdmin(admin.ModelAdmin):  
    list_display=('descricao','image_tag')

## Administração dos Serviços
class ServicoAdmin(admin.ModelAdmin):
    list_display=('titulo','image_tag')

## Administração da Páginas
class PaginaAdmin(admin.ModelAdmin):
    list_display=('titulo',)
    
## Administração dos Faqs
class FaqAdmin(admin.ModelAdmin):
    list_display=('pergunta',)

    
## Administração dos Formulários
class FormularioAdmin(admin.ModelAdmin):
    list_display=('nome_completo','email','detalhes','tempo_envio')
    
## Administração do Grupo de Galeria
class GaleriaAdmin(admin.ModelAdmin):
    list_display=('titulo','descricao','image_tag',)
    
## Administração de Imagens de tal grupo da Galeria <Relação muito para muitos>
class GaleriaFotosAdmin(admin.ModelAdmin):
    list_display=('descricao','image_tag',)

## Edição do Footer
class FooterAdmin(admin.ModelAdmin):
    list_display=('descricao',)


## Administração dos Planos
class SubPlanAdmin(admin.ModelAdmin):
    list_editable=('highlight_status',)
    list_display=('title','price','highlight_status','validity_days')
    

## Detalhes dos planos
class SubPlanFeaturesAdmin(admin.ModelAdmin):
    list_display=('title','subplans')
    
    def subplans(self,obj):
        ## Retorna os planos separados por | (Ex: Básico | Médio | Avançado)
        return " | ".join([sub.title for sub in obj.subplan.all()])



## Administração dos clientes
class SubscriberAdmin(admin.ModelAdmin):
    list_display=('user','image_tag','celular')

## Administração da Subinscrição dos planos    
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=('user','plan','reg_date','price')


# Administração de Treinadores
class TrainerAdmin(admin.ModelAdmin):
	list_editable=('is_active',)
	list_display=('full_name','mobile','salary','is_active','image_tag')    

# Administração de Notificações
class NotifyAdmin(admin.ModelAdmin):
    list_display=('notify_detail','read_by_user','read_by_trainer')

# Administração de ligar Cliente para Treinador
class AssignSubscriberAdmin(admin.ModelAdmin):
    list_display=('trainer','user') 

# Conquistas do Treinador
class TrainerAchivementAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')

class TrainerSalaryAdmin(admin.ModelAdmin):
	list_display=('trainer','amt','amt_date')
 

## Notificação do treinador
class TrainerNotificationAdmin(admin.ModelAdmin):
    list_display=('notif_msg',)

class TrainerNotificationStatusAdmin(admin.ModelAdmin):
    list_display=('notif',)
    
## Mensagem Treinador
class TrainerMsgAdmin(admin.ModelAdmin):
    list_display=('user','trainer','message')   


## Relatório para Usuário
class TrainerSubscriberReport(admin.ModelAdmin):
    list_display=('report_msg','report_for_trainer','report_for_user','report_from_trainer','report_from_user')
 
## Logomarca
class LogoAdmin(admin.ModelAdmin):
    list_display=('logo_img',)   
   
# Registra as abas na página de administração
admin.site.register(models.Banners,BannerAdmin)
admin.site.register(models.Servicos,ServicoAdmin)
admin.site.register(models.Pagina,PaginaAdmin)
admin.site.register(models.Faq,FaqAdmin)
admin.site.register(models.Formulario,FormularioAdmin)
admin.site.register(models.Galeria,GaleriaAdmin)
admin.site.register(models.GaleriaFotos,GaleriaFotosAdmin)
admin.site.register(models.Footer,FooterAdmin)
admin.site.register(models.SubPlan,SubPlanAdmin)
admin.site.register(models.SubPlanFeature,SubPlanFeaturesAdmin)
admin.site.register(models.Subscriber,SubscriberAdmin)
admin.site.register(models.Subscription,SubscriptionAdmin)
admin.site.register(models.Trainer,TrainerAdmin)
admin.site.register(models.Notify,NotifyAdmin)
admin.site.register(models.AssignSubscriber,AssignSubscriberAdmin)
admin.site.register(models.TrainerAchivement,TrainerAchivementAdmin)
admin.site.register(models.TrainerSalary,TrainerSalaryAdmin)
admin.site.register(models.TrainerNotification,TrainerNotificationAdmin)
admin.site.register(models.TrainerMsg,TrainerMsgAdmin)
admin.site.register(models.NotifTrainerStatus,TrainerNotificationStatusAdmin)
admin.site.register(models.TrainerSubscriberReport,TrainerSubscriberReport)
admin.site.register(models.AppSetting,LogoAdmin)