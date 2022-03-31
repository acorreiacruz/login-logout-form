from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    form = LoginForm()
    return render(request, 'users/pages/login.html', context={
        'form': form,
        'form_action': "/"
    })
