from django.db import models

# Create your models here.
class AddUser(models.Model):
    name = models.CharField(max_length = 25)
    email = models.EmailField()
    password = models.CharField(max_length = 40)

