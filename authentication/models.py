from django.db import models

# Create your models here.


from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
       if not (email and username):
           raise ValueError('User must have an email address')
       user = self.model(email=self.normalize_email(email))
       user.set_password(password)
       user.save(using=self.db)
       return user
        

     
#https://localhost:8000/oauth/complete/google-oauth2/
    def create_superuser(self, email,username=None, password=None):
        user = self.create_user(email, username, password=password)
        user.is_admin=True
        user.save(using=self.db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, null=True,unique=False)
    
    

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    owner = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')
    about = models.CharField(max_length=250, blank=True)
    verification_token = models.CharField(max_length=250, blank=True, null=True)
    


    def __str__(self):
        return self.owner.email


