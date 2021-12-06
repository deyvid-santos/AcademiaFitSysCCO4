from django.shortcuts import render, redirect
from academiafitApp import models
from academiafitApp import forms
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from datetime import timedelta

import stripe

# Create your views here.

# Página Home
from academiafitApp.forms import SignUp


def home(request):
    banners = models.Banners.objects.all()
    servicos = models.Servicos.objects.all()
    gimgs = models.GaleriaFotos.objects.all().order_by('id')
    footer = models.Footer.objects.first()
    return render(request, 'home.html', {'banners': banners, 'servicos': servicos, 'gimgs': gimgs, 'footer':footer})
    # após home.html, {<titulo do objeto no arquivo html>:<objeto que instancia tudo do nosso modelo>}

# Serviços Páginas
def servicopagina(request, id):
    servico = models.Servicos.objects.get(id=id)
    footer=models.Footer.objects.first()
    return render(request, 'servicopagina.html',({'servico':servico,'footer':footer}))

# Página customizada gerada
def pagina_desc(request, id):
    pagina = models.Pagina.objects.get(id=id)
    footer = models.Footer.objects.first()
    return render(request, 'paginas.html', {'pagina': pagina,'footer':footer})


#  Página de Faqs
def faq_list(request):
    faq = models.Faq.objects.all()
    footer = models.Footer.objects.first()
    return render(request, 'faq.html', {'faq': faq,'footer':footer})


# Página de Formulário
def formulario(request):
    # A condicional abaixo, checa a solicitação do usuário e valida o formulário dando uma mensagem na variável msg
    footer = models.Footer.objects.first()
    msg = ''
    if request.method == 'POST':
        form = forms.FormularioForm(request.POST)
        if form.is_valid:
            form.save()
            msg = 'O formulário foi salvo com sucesso!'
    form = forms.FormularioForm
    return render(request, 'formulario.html', {'form': form, 'msg': msg,'footer':footer})


# Página de Galeria <grupo>
def galeria(request):
    galeria = models.Galeria.objects.all().order_by('titulo')
    footer = models.Footer.objects.first()
    return render(request, 'galeria.html', {'galeria': galeria,'footer':footer})


def galeria_foto(request, id):
    galeria = models.Galeria.objects.get(id=id)
    galeria_imgs = models.GaleriaFotos.objects.filter(galeria=galeria).order_by('descricao')
    footer = models.Footer.objects.first()
    return render(request, 'galeria_imgs.html', {'galeria_imgs': galeria_imgs, 'galeria': galeria,'footer':footer})


# Página de Registro
def signup(request):
    footer = models.Footer.objects.first()
    msg = None
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Obrigado por se registrar.'
    form = forms.SignUp
    return render(request, 'registration/signup.html', {'form': form, 'msg': msg,'footer':footer})

# Plano
def pricing(request):
    footer = models.Footer.objects.first()
    pricing=models.SubPlan.objects.all()
    dfeatures=models.SubPlanFeature.objects.all()
    return render(request, 'pricing.html',{'plans':pricing,'dfeatures':dfeatures,'footer':footer})


# Checkout (Pagamentos)
def checkout(request,plano_id):
    footer = models.Footer.objects.first()
    planoDetalhe=models.SubPlan.objects.get(pk=plano_id)
    return render(request, 'checkout.html',{'plan':planoDetalhe,'footer':footer})

# Sessão de pagamento utlizando Stripe 
# https://stripe.com/docs/api/authentication

    """
    
    Sessão do Stripe
        - ID do Plano
        - Sessão criada
          + Tipo de pagamento - Cartão
          + Itens: Preço, 
                   Tipo da moeda, 
                   Dado do produto, 
                   Nome do Plano,
                Unidade : Preço do plano * 100
            Quantidade: 1 (Já que um plano)
        Modo -> Pagamento
        URL de Sucesso (127.0.0.1/pay_success? <Chave da sessão>
        URL de Erro (127.0.0.1/pay_cancel? <Chave da sessão>)
        Clinte tem instância com o plano    
    return -> redirecionamento das páginas
    """
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
def checkout_session(request,plan_id):
	plan=models.SubPlan.objects.get(pk=plan_id)
	session=stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
	      'price_data': {
	        'currency': 'brl',
	        'product_data': {
	          'name': plan.title,
	        },
	        'unit_amount': plan.price*100,
	      },
	      'quantity': 1,
	    }],
	    mode='payment',
	    success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
	    cancel_url='http://127.0.0.1:8000/pay_cancel',
        client_reference_id=plan_id
	)
	return redirect(session.url, code=303)

# Successo na compra
# https://stripe.com/docs/api/checkout/sessions/create?lang=python
def pay_success(request):
    footer = models.Footer.objects.first()
    # Sessão da API é gerada com um key para segurança
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id = session.client_reference_id
    plan = models.SubPlan.objects.get(pk=plan_id)
    user = request.user
    models.Subscription.objects.create(plan=plan,
                                       user=user,
                                       price=plan.price)
    
    # Alerta no e-mail
    subject = 'Pagamento da AcademiaFIT'
    html_content = get_template('orderemail.html').render({'title':plan.title})
    from_email = 'administracao@academiafit.com.br'
    useremail = User.email
    msg = EmailMessage(subject, html_content, from_email, [useremail])
    msg.content_subtype = "html"
    msg.send()
    return render(request, 'success.html',{'footer':footer})


# Erro na compra
def pay_cancel(request):
    footer = models.Footer.objects.first()
    return render(request, 'cancel.html',{'footer':footer})

# Dashboard
def user_dashboard(request):
    footer = models.Footer.objects.first()
    current_plan=models.Subscription.objects.get(user=request.user)
    my_trainer=models.AssignSubscriber.objects.get(user=request.user)
    enddate=current_plan.reg_date+timedelta(days=current_plan.plan.validity_days)

	# Notificações
    data=models.Notify.objects.all().order_by('-id')
    notifStatus=False
    jsonData=[]
    totalUnread=0
    for d in data:
        try:
            notifStatusData=models.NotifUserStatus.objects.get(user=request.user,notif=d)
            if notifStatusData:
                notifStatus=True
        except models.NotifUserStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totalUnread=totalUnread+1

    return render(request, 'user/dashboard.html',{
        'current_plan':current_plan,
        'my_trainer':my_trainer,
        'total_unread':totalUnread,
        'enddate':enddate,
        'footer':footer
    })

# Formulário de edição de senha
def update_profile(request):
    footer = models.Footer.objects.first()
    msg=None
    if request.method=='POST':
        form=forms.ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            msg='O dado foi salvo'
    form=forms.ProfileForm(instance=request.user)
    return render(request, 'user/update-profile.html',{'form':form,'msg':msg, 'footer':footer})

# Login do treinador
def trainerlogin(request):
    footer = models.Footer.objects.first()
    msg=''
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']
        trainer=models.Trainer.objects.filter(username=username,pwd=pwd).count()
        if trainer > 0:
            trainer=models.Trainer.objects.filter(username=username,pwd=pwd).first()
            request.session['trainerLogin']=True
            request.session['trainerid']=trainer.id
            return redirect('/trainer_dashboard')
        else:
            msg='Dados inválidos'
    form=forms.TrainerLoginForm
    return render(request, 'trainer/login.html',{'form':form,'msg':msg,'footer':footer})

# Trainer Logout
def trainerlogout(request):
    del request.session['trainerLogin']
    return redirect('/trainerlogin') 

# Dashboard do Treinador
def trainer_dashboard(request):
    footer = models.Footer.objects.first()
    return render(request, 'trainer/dashboard.html', {'footer':footer})

# Perfil do Treinador
def trainer_profile(request):
    footer=models.Footer.objects.first()
    t_id=request.session['trainerid']
    trainer=models.Trainer.objects.get(pk=t_id)
    msg=None
    
    if request.method=='POST':
        form=forms.TrainerProfileForm(request.POST,request.FILES,instance=trainer)
        if form.is_valid():
            form.save()
            msg='O perfil foi atualizado'
        
    form=forms.TrainerProfileForm(instance=trainer)
    return render(request, 'trainer/profile.html',{'form':form,'msg':msg,'footer':footer})
    
    
# Notificação
def notifs(request):
    footer = models.Footer.objects.first()
    data=models.Notify.objects.all().order_by('-id')
    return render(request, 'notifs.html',{'footer':footer})

#  Getters das Notificações
    """
       -- Ajax -- 
    """
def get_notifs(request):
    data=models.Notify.objects.all().order_by('-id')
    notifStatus=False
    jsonData=[]
    totalUnread=0
    
    for d in data:
        try:
            notifStatusData=models.NotifUserStatus.objects.get(user=request.user,notif=d)
            if notifStatusData:
                notifStatus=True
        except models.NotifUserStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totalUnread=totalUnread+1
        jsonData.append({
            'pk':d.id,
            'notify_detail':d.notify_detail,
            'notifStatus':notifStatus
        })
        
    return JsonResponse({'data':jsonData,'totalUnread':totalUnread})

# Marcar como lido
def mark_read_notif(request):
    notif=request.GET['notif']
    notif=models.Notify.objects.get(pk=notif)
    user=request.user
    models.NotifUserStatus.objects.create(notif=notif,user=user,status=True)
    return JsonResponse({'bool':True})


# Clientes do Treinador
def trainer_subscribers(request):
    footer = models.Footer.objects.first()
    trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
    trainer_subs=models.AssignSubscriber.objects.filter(trainer=trainer).order_by('-id')
    return render(request, 'trainer/trainer_subscriber.html',{'trainer_subs':trainer_subs,'footer':footer})

# Pagamentos do Treinador
def trainer_payments(request):
    footer = models.Footer.objects.first()
    trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
    trainer_pays=models.TrainerSalary.objects.filter(trainer=trainer).order_by('-id')
    return render(request, 'trainer/trainer_payments.html',{'trainer_pays':trainer_pays,'footer':footer})


#Alterar senha do treinador
def trainer_changepassword(request):
    footer = models.Footer.objects.first()
    msg=None
    if request.method=='POST':
        new_password=request.POST['new_password']
        updateRes=models.Trainer.objects.filter(pk=request.session['trainerid']).update(pwd=new_password)
        if updateRes:
            del request.session['trainerLogin']
            return redirect('/trainerlogin')
        else:
            msg='Algo deu errado.'
    form=forms.TrainerChangePassword
    return render(request, 'trainer/trainer_changepassword.html',{'form':form,'footer':footer})


def trainer_notifs(request):
    footer=models.Footer.objects.first()
    data=models.TrainerNotification.objects.all().order_by('-id')
    trainer=models.Trainer.objects.get(id=request.session['trainerid'])
    totalUnread=0
    jsonData=[]
    for d in data:
        try:
            notifStatusData=models.NotifTrainerStatus.objects.get(trainer=trainer,notif=d)
            if notifStatusData:
                notifStatus=True
        except models.NotifTrainerStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totaUnread=totalUnread+1
            jsonData.append({
                'pk':d.id,
                'notify_detail':d.notif_msg,
                'notifStatus':notifStatus
            })
    
    return render(request, 'trainer/notifs.html',{'notifs':jsonData,'totalUnread':totalUnread,'footer':footer})

# Marcar como lido (Treinador)
def mark_read_trainer_notif(request):
    notif=request.GET['notif']
    notif=models.TrainerNotification.objects.get(pk=notif)
    trainer=models.Trainer.objects.get(id=request.session['trainerid'])
    models.NotifTrainerStatus.objects.create(notif=notif,trainer=trainer,status=True)
    
    # Contar não lidos
    totalUnread = 0
    data=models.TrainerNotification.objects.all().order_by('-id')
    for d in data:
        try:
            notifStatusData=models.NotifTrainerStatus.objects.get(trainer=trainer,notif=d)
            if notifStatusData:
                notifStatus=True
        except models.NotifTrainerStatus.DoesNotExist:
            notifStatus=False
        if not notifStatus:
            totalUnread=totalUnread+1
            
    return JsonResponse({'bool':True,'totalUnread':totalUnread})


# Mensagens do treinador
def trainer_msgs(request):
    footer=models.Footer.objects.first()
    data=models.TrainerNotification.objects.all().order_by('-id')
    return render(request, 'trainer/notifs.html',{'notifs':data,'footer':footer})


# Report for user
def report_for_user(request):
    footer = models.Footer.objects.first()
    trainer=models.Trainer.objects.get(id=request.session['trainerid'])
    msg=''
    if request.method=='POST':
        form=forms.ReportForUserForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.report_from_trainer=trainer
            new_form.save()
            msg='O dado foi salvo'
        else:
            msg='Dados inválidos'
    form=forms.ReportForUserForm
    return render(request, 'report_for_user.html',{'form':form,'msg':msg,'footer':footer})

# Report for trainer
def report_for_trainer(request):
    footer = models.Footer.objects.first()
    user=request.user
    msg=''
    if request.method=='POST':
        form=forms.ReportForTrainerForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.report_from_user=user
            new_form.save()
            msg='O dado foi salvo'
        else:
            msg='Dados inválidos'
    form=forms.ReportForTrainerForm
    return render(request, 'trainer/report_for_trainer.html',{'form':form,'msg':msg,'footer':footer})    