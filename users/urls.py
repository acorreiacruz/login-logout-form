from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/validate/', views.login_view_validate, name="login_validate"),
    path('register/', views.register, name="register"),
    path('regiser/validate/', views.register_validate, name="register_validate"),
]
