from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError('User must have a valid email address')
        user = self.model(email= self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Customized user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Course(models.Model):

    title = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    award = models.CharField(max_length=255)
    ects_credits = models.CharField(max_length=255)
    mode = models.CharField(max_length=255)
    deadline = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    nfq = models.CharField(max_length=255)
    ote_flag = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)



    def __str__(self):
        return self.title









