from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import LoginForm, RegisterLogin

def login_view(request):
    form_data = request.session.get("form_data")
    form = LoginForm(form_data)
    return render(request, 'users/pages/login.html', context={
        'form': form,
        'form_action': reverse("users:login_validate"),
    })

def login_view_validate(request):
    if request.GET:
        raise Http404()
    
    form = LoginForm()
