from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import uuid


# Create your models here.
class ConnectionState(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=80)


class ManagerUser(BaseUserManager):
    def create_user(self, name, last_name, email, phone, password=None):
        user = self.model(name=name, last_name=last_name, email=email, phone=phone)

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    username = models.UUIDField(default=uuid.uuid4, unique=True)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=64, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False, unique=True)
    state = models.ForeignKey(ConnectionState, on_delete=models.DO_NOTHING, default="1")

    objects = ManagerUser()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "Users"
        ordering = ['id']
        verbose_name = "user"
