from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone


class Usermanager(BaseUserManager):
    def _create_user(self,name,email,password,**extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email,name=name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,name=None,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(name,email,password,**extra_fields)
    
    def create_superuser(self,name=None,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(name,email,password,**extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length= 50,null=True,blank=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True,null=True)
    
    objects = Usermanager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return self.name
    
    
    