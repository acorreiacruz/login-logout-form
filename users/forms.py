from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    
    username = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ':',
        help_text = "Digite o seu nome de usuário",
        widget = forms.TextInput(attrs = {
            'placeholder': 'Nome de usuário',
        }),
        error_messages = {
            'required': 'O campo de usuário não pode ficar vazio, insira o seu nome de usuário!',
            'invalid':'Nome de usuário inválido, repita o processo e insira um válido!',
        }
    )

    password = forms.CharField(
        required = True,
        label = 'Senha',
        label_suffix = ':',
        help_text = 'Digite a sua senha de login',
        widget = forms.PasswordInput(attrs = {
            'placeholder':'Digite a sua senha aqui',
        }),
        error_messages= {
            'required': 'O campo de senha não pode ficar vazio, insira a sua senha!',
            'invalid':'Senha inserida inválida, repita o processor e insira uma válida!',
        }
    )


class RegisterLogin(forms.ModelForm):

    first_name = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ":",
        help_text = "Digite o seu nome de usuário",
        widget = forms.TextInput(attrs = {
                'placeholder':'',       
        }),
        error_messages = {
            'required':'O campo de primeiro nome não pode ficar vazio, insira um valor!',
            'invalid':'O primeiro nome inserido é inválido!, insira um válido!',
        }
    )

    last_name = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ":",
        help_text = "Digite o seu nome de usuário",
        widget = forms.TextInput(attrs = {
                'placeholder':'',    
        }),
        error_messages = {
            'required':'O campo de primeiro nome não pode ficar vazio, insira um valor!',
            'invalid':'O primeiro nome inserido é inválido!, insira um válido!',
        }
    )

    username = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ":",
        help_text = "Digite o seu nome de usuário",
        widget = forms.TextInput(attrs = {
                'placeholder':'',   
        }),
        error_messages = {
            'required':'',
            'invalid':'',
        }
    )

    email = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ":",
        help_text = "Digite o seu nome de usuário",
        widget = forms.TextInput(attrs = {
                'placeholder':'', 
        }),
        error_messages = {
            'required':'',
            'invalid':'',
        }
    )

    password = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ":",
        help_text = "Digite o seu nome de usuário",
        widget = forms.PasswordInput(attrs = {
                'placeholder':'',
            
        }),
        error_messages = {
            'required':'',
            'invalid':'',
        }
    )

    password_confirmation = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ":",
        help_text = "Digite o seu nome de usuário",
        widget = forms.PasswordInput(attrs = {
                'placeholder':'',
            
        }),
        error_messages = {
            'required':'',
            'invalid':'',
        }
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    
