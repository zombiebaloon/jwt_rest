from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,BaseUserManager, UserManager
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is require')
        email = self.normalize_email(email)
        user = self.model(email= email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is staff true'))

        return self.create_user(email,password, **extra_fields)





class User(AbstractUser):
    # phone_regex = RegexValidator( regex =r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: +999999999. Up to 14 digits allowed.")
    username = models.CharField(unique=True,blank=True,null=True,max_length=255)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    objects = UserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
