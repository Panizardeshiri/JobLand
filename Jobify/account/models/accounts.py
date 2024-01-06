from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser

# Define CustomUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(({'error' : {'detail': "This Field is required!"}} ))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(("Superuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(("Superuser must have is_superuser=True"))
        return self.create_user(email, password, **extra_fields)





# Define CustomUser
class User(PermissionsMixin,AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    Gender = (
    ('M','MALE'),
    ('F','FEMALE'),
)
    gender = models.CharField( max_length=2, choices=Gender)
    UserType = (
    ('employee','EMPLOYEE'),
    ('employer','EMPLOYER'),
)
    user_type = models.CharField( max_length=20, choices=UserType, default=UserType[0][0] )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
