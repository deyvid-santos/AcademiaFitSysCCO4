from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput

from academiafitApp import models

class FormularioForm(forms.ModelForm):
    class Meta:
        model=models.Formulario
        fields=('nome_completo','email','detalhes')

class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')

class ProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','username',)
        
"""
    Página de Login do Treinador
    + Usuário
    + Senha
"""       
class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model=models.Trainer
        fields=('username','pwd')
        widgets = {
            'pwd':forms.PasswordInput
        }        

class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model=models.Trainer
        fields=('full_name','mobile','address','detail','img')
        
class TrainerChangePassword(forms.Form):
    new_password=forms.CharField(max_length=50,required=True,label='Nova senha')

class ReportForUserForm(forms.ModelForm):
    class Meta:
        model=models.TrainerSubscriberReport
        fields=('report_for_user','report_msg','report_from_trainer')
        widgets = {'report_from_trainer': forms.HiddenInput()}
        labels = {
            'report_for_user':'Para o usuário:',
            'report_msg':'Mensagem',
        }

class ReportForTrainerForm(forms.ModelForm):
    class Meta:
        model=models.TrainerSubscriberReport
        fields=('report_for_trainer','report_msg','report_from_user')
        labels={
            'report_for_trainer':'Para o treinador:',
            'report_msg':'Mensagem',
        }
        widgets = {'report_from_user': forms.HiddenInput()} 