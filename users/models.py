from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20,null=True, blank = True)
    email = models.EmailField(_('email address'),unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='uploads',blank=True)

    
