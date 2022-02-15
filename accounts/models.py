from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self,email,username,phone,password):
        if not email:
            raise ValueError('please enter email: ')
        if not username:
            raise ValueError('please enter username: ')
        if not phone:
            raise ValueError('please enter phone: ')
        user = self.model(email=self.normalize_email(email),username=username,phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,phone,password):
        user = self.create_user(email=email,username=username,phone=phone,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

        


class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    # FirstName = models.CharField(max_length=255)
    # LastName = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

    
