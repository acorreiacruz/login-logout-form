from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
            'invalid':'Senha inserida inválida, repita o processo e insira uma válida!',
        }
    )


class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(
        required = True,
        label = "Primeiro Nome",
        label_suffix = ":",
        help_text = "Digite o seu primeiro nome",
        widget = forms.TextInput(attrs = {
                'placeholder':'Ex.: antonio',       
        }),
        error_messages = {
            'required':'O campo de primeiro nome não pode ficar vazio, insira um valor!',
            'max-length':"O primeiro nome deve ter no máximo 20 caracteres",
            'min-length':'O primeiro nome deve ter no mínimo 5 caracteres',
        },
        max_length = 20,
        min_length= 3,
    )

    last_name = forms.CharField(
        required = True,
        label = "Último Nome",
        label_suffix = ":",
        help_text = "Digite o seu último nome",
        widget = forms.TextInput(attrs = {
                'placeholder':'Ex.: correia',    
        }),
        error_messages = {
            'required':'O campo de último nome não pode ficar vazio, insira um valor!',
            'max-length':"O último nome deve ter no máximo 20 caracteres",
            'min-length':'O último nome deve ter no mínimo 3 caracteres',
        },
        max_length = 20,
        min_length = 3,
    )

    username = forms.CharField(
        required = True,
        label = "Nome de usuário",
        label_suffix = ":",
        help_text = "Digite o seu nome de usuário",
        widget = forms.TextInput(attrs = {
                'placeholder':'Ex.: antoniocorreia',   
        }),
        error_messages = {
            'required':'O campo de nome de usuário não pode ficar vazio, insira um valor!',
        },
    )

    email = forms.EmailField(
        required = True,
        label = "E-mail",
        label_suffix = ":",
        help_text = "Digite o seu endereço de e-mail",
        widget = forms.EmailInput(attrs = {
                'placeholder':'Ex.: email@email.com', 
        }),
        error_messages = {
            'required':'O campo de e-mail não pode ficar vazio, insira um valor!',
            'invalid':'Endereço de e-mail inválido, insira um válido!',
        },
    )

    password = forms.CharField(
        required = True,
        label = "Senha",
        label_suffix = ":",
        help_text = "Digite uma senha",
        widget = forms.PasswordInput(attrs = {
                'placeholder':'Senha',
        }),
        error_messages = {
            'required':'O campo de senha não pode ficar vazio, insira um valor!',
        },
    )

    password_confirmation = forms.CharField(
        required = True,
        label = "Confirmação da Senha",
        label_suffix = ":",
        help_text = "Digite novamente a sua senha",
        widget = forms.PasswordInput(attrs = {
                'placeholder':'Confirmação da senha',
        }),
        error_messages = {
            'required':'O campo de confirmação de senha não pode ficar vazio, insira um valor!',
        },
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password','password_confirmation']

    def clean_username(self):
        username_data = self.cleaned_data.get('username','')
        exist = User.objects.filter(
            username = username_data,
        ).exists()

        if exist:
            raise ValidationError(
                "Nome de usuário já cadastrado, insira um novo!",
                code="invalid",
            )
       
        return username_data

    def clean_email(self):
        email_data = self.cleaned_data.get("email")
        exist = User.objects.filter(
            email = email_data
        ).exists()

        if exist:
            raise ValidationError(
                "Endereço de e-mail já cadastrado, insira um novo!",
                code = "invalid",
            )

        return email_data

    def clean(self):
        cleaned_data = super().clean()
        password_data = cleaned_data.get("password")
        password_confirmation_data = cleaned_data.get("password_confirmation")

        if password_data != password_confirmation_data:
            raise ValidationError({
                "password": ValidationError(
                    "Ambas as senhas devem ser iguais!",
                    code = "invalid",
                ),
                "password_confirmation": ValidationError(
                    "Ambas as senhas devem ser iguais!",
                    code = "invalid",
                ),
            })
        



    
