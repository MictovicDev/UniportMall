from django.contrib import admin
from django.urls import path
from . import views
from .views import RegisterView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('', views.home, name='home'),
    path('validate-username', csrf_exempt(views.UsernameValidationView.as_view()), name='validate_username'),
    path('validate-email', csrf_exempt(views.EmailValidationView.as_view()), name='validate_email'),
    path('validate-password', csrf_exempt(views.PasswordValidator.as_view()), name='validate_password'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', views.login, name='login'),
    path('verify/<str:verification_token>', views.verify_account, name='verify')

]

# print(settings.SITE_URL+'/verify/<str:verification_token>')