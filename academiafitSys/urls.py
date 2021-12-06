"""academiafitSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from academiafitApp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('paginadesc/<int:id>',views.pagina_desc,name='paginadesc'),
    path('faqs',views.faq_list,name='faq'),
    path('formulario',views.formulario,name='formulario'),
    path('ckeditor', include("ckeditor_uploader.urls")),
    path('servicopagina/<int:id>',views.servicopagina,name='servicopagina'),
    
    # Galeria
    path('galeria',views.galeria,name='galeria'),
    path('galeriafoto/<int:id>',views.galeria_foto,name='galeria_foto'),
    
    # Conta
    path('accounts/signup',views.signup,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Pagamento
    path('pricing/',views.pricing,name='pricing'),
    path('checkout/<int:plano_id>', views.checkout, name='checkout'),
    path('checkout_session/<int:plan_id>',views.checkout_session,name='checkout_session'),
	path('pay_success',views.pay_success,name='pay_success'),
	path('pay_cancel',views.pay_cancel,name='pay_cancel'),
 
    # Usuário
    path('user-dashboard',views.user_dashboard,name='user_dashboard'),
    path('update-profile',views.update_profile,name='update_profile'),
    
    # Treinador
    path('trainerlogin',views.trainerlogin,name='trainerlogin'),
    path('trainerlogout',views.trainerlogout,name='trainerlogout'),
    path('trainer_dashboard',views.trainer_dashboard,name='trainer_dashboard'),
    path('trainer_profile',views.trainer_profile,name='trainer_profile'),
    path('trainer_subscribers',views.trainer_subscribers,name='trainer_subscribers'),
    path('trainer_payments',views.trainer_payments,name='trainer_payments'),
    path('trainer_changepassword',views.trainer_changepassword,name='trainer_changepassword'),
    path('trainer_notifs',views.trainer_notifs,name='trainer_notifs'),
    path('messages',views.trainer_msgs,name='messages'),
    path('report_for_trainer',views.report_for_trainer,name='report_for_trainer'),
    
    #Notificações e Mensagens
    path('notifs',views.notifs,name='notifs'),
    path('get_notifs',views.get_notifs,name='get_notifs'),
    path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
    path('report_for_user',views.report_for_user,name='report_for_user'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
