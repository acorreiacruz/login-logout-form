from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

def register(request):

    register_form_data = request.session.get("register_form_data",None)
    form = RegisterForm(register_form_data)

    return render(request, 'users/pages/register.html', context={
        'form': form,
        'form_action': reverse("users:register_validate"),
    })

def register_validate(request):

    if not request.POST:
        raise Http404()

    register_form_data = request.POST
    request.session['register_form_data'] = register_form_data

    form = RegisterForm(register_form_data)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        form.save()
        del(request.session['register_form_data'])
        return redirect("users:login")

    return redirect('users:register')

def login_view(request):

    form = LoginForm()
    
    return render(request,'users/pages/login.html',context={
        'form': form,
        'form_action': reverse("users:login_validate")
    })

def login_view_validate(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )

        if authenticated_user is not None:
            messages.success("Usuário logado com sucesso!")
            login(request,authenticated_user)
        else:
            messages.error("Credenciais do usuário inválidas!")
            
    else:
        messages.error("Nome de usuário e senha inválidos!")
    
    return redirect("users:login")

@login_required(login_url="users:login",redirect_field_name="next")
def logout_view(request):
    logout(request)
    return redirect("users:login")


