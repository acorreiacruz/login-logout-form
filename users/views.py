from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib import messages

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
        ...
    


