from django.shortcuts import render, redirect
from django.views import View
from .models import *
import json
from django.http import JsonResponse
from django.contrib import messages
from django.contrib import auth 
from . import emailvalidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your views here.
@receiver(post_save, sender=MyUser)
def profile(sender, instance, **kwargs):
    profile = Profile.objects.filter(owner=instance.id)
    if not profile:
        verification_token = get_random_string(length=32)
        new_profile = Profile.objects.create(owner=instance, verification_token=verification_token)
    



class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'}, status=400)
        # if MyUser.objects.filter(username=username).exists():
        #     return JsonResponse({'username_error':'sorry user with username already exists'}, status=409)
            
        return JsonResponse({'username_valid': True})

def send_verification_email(user_email,user, verification_token):
    subject = 'Account Verification'
    message = render_to_string('authentication/verify_email.html', {
        'verification_token': verification_token,
        'site_url': settings.SITE_URL,
        'username': user.username
    })
    plain_message = strip_tags(message)
    email = EmailMultiAlternatives(subject, plain_message,settings.DEFAULT_FROM_EMAIL, [user_email])
    email.attach_alternative(message, "text/html")
    email.send()

def verify_account(request, verification_token):
    user_profile = Profile.objects.get(verification_token=verification_token)
    if user_profile:
        user = user_profile.owner
        user.is_active = True
        user.save()
        user_profile.verification_token = None
        user_profile.save()
        messages.success(request, 'Verification Succesful')
        
        return redirect('login')
    else:
        return render(request, 'verification_error.html')

class RegisterView(View):

    def post(self,request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        request.session['email'] = email
        request.session['password'] = password

        

        print(request.POST)

        context = {
            'fieldValues': request.POST
        }
        user_exists = MyUser.objects.filter(email=email).exists()
        if not user_exists:
            user = MyUser.objects.create(email=email,username=username)
            user.set_password(password)
            user.username = username
            user.save()
            verification_token = user.profile.verification_token
            send_verification_email(email, user, verification_token)
            messages.success(request, 'Please click the Link in your mail to verify account')
            if settings.DEBUG:
                return redirect('login')
            else:
                return redirect('register')
        messages.error(request, 'Please fill in your details')
        return render(request, 'authentication/register.html',context)

    def get(self, request):
        return render(request, 'authentication/register.html')

def login(request):
    if request.method =='POST':
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = MyUser.objects.filter(email=email)
        except:
            messages.error(request, 'User does not exists')
        user = auth.authenticate(request, email=email, password=password,)
        print('authenticated')
        if user is not None:
             print(user)
             auth.login(request, user)
             return redirect('home')
        print(user)
        messages.error(request, 'user does not exists')
        return render(request, 'authentication/login.html')


    if request.method == 'GET':
        email = request.session.get('email')
        password = request.session.get('password')
        
        if email and password:
            context = {
                'email': email,
                'password' : password
            }
        else:
            context =None
        return render(request, 'authentication/login.html',context)


class EmailValidationView(View):

    def validateemail(email):
        for x in email:
            if type(x) == int:
                return False
            ans = email.split('.')
            second = ans.pop()
        for x in ans:
            for i in x:
                if i == '@':
                    if second == 'com':
                        return True

        return False


    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        result = EmailValidationView.validateemail(email)

        if not result:
            return JsonResponse({'email_error':'input a valid email'}, status=400)
        if MyUser.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry user with email already exists'}, status=409)
            
        return JsonResponse({'email_valid': True})

class PasswordValidator(View):

    def checkpassword(password):
        for x in range(len(password)):
            if len(password) < 6:
                return False
            else:
                return True

    def post(self, request):
        data = json.loads(request.body)
        password = data['password']
        result = PasswordValidator.checkpassword(password)
        if not result:
           return JsonResponse({'password_error':'password should be greater than six characters'},status=400)
        return JsonResponse({'password_valid':True})



def home(request):
    return render(request, 'authentication/home.html')

def register(request):
    return render(request, 'authentication/register.html')



