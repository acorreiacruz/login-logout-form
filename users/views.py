from django.shortcuts import render


def login(request):
    
    render(request,'users/pages/login.html')
