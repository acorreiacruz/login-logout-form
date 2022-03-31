from django.shortcuts import redirect, render
from .forms import LoginForm

def login_view(request):

    form = LoginForm()
    return render(request, 'users/pages/login.html', context={
        'form': form,
        
    })

def login_view_validate(request):
    ...