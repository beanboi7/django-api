from django.db import models
import uuid

# Create your models here.
class AddUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 25)
    email = models.EmailField()
    password = models.CharField(max_length = 40)

