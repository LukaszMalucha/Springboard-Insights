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

    title = models.CharField(max_length=255, default="none")
    provider = models.CharField(max_length=255, default="none")
    award = models.CharField(max_length=255, default="none")
    ects_credits = models.CharField(max_length=255, default="none")
    mode = models.CharField(max_length=255, default="none")
    deadline = models.CharField(max_length=255, default="none")
    start_date = models.CharField(max_length=255, default="none")
    end_date = models.CharField(max_length=255, default="none")
    nfq = models.CharField(max_length=255, default="none")
    ote_flag = models.CharField(max_length=255, default="none")
    link = models.CharField(max_length=255, default="none")
    skills = models.CharField(max_length=255, default="none")
    delivery = models.CharField(max_length=255, default="none")



    def __str__(self):
        return self.title









