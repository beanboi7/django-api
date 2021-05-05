from django.db import models
import uuid

# Create your models here.
class AddUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length = 25)
    email = models.EmailField()
    password = models.CharField(max_length = 40)
 


# from django.contrib.auth.hashers import make_password

# class UserManager(BaseUserManager):
#     def create_user(self, email, username, password, alias=None):
#         user = self.model(
#         email = self.normalize_email(email),
#                 username = username,)
#         user.set_password(password)
#         user.save()
#         return user
#     def create_superuser(self, email, username, password):
#        self.create_user(email, username, password)
#        user.is_staff()
#        user.is_superuser = True
#        user.save()
#        return user

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(null=False, unique=True)
#     username = models.CharField(max_length=25, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username",]


# def validate_password(self, value: str) -> str:
#     """
#     Hash value passed by user.
#     :param value: password of a user
#     :return: a hashed version of the password
#     """
#     return make_password(value)