from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import time
from core.utils import content_file_name


# Manager Class
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError('User must have a valid email address')
        if len(str(password)) < 8:
            raise ValueError('This password is too short. It must contain at least 8 characters.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.name = "Admin"
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Model Class
class User(AbstractBaseUser, PermissionsMixin):
    """Customized user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        MyProfile.objects.get_or_create(owner=self)


class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default='guest', blank=True)
    image = models.ImageField(upload_to=content_file_name, default='portraits/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.owner) + " profile"


class Course(models.Model):

    title = models.CharField(max_length=255, default="none")
    provider = models.CharField(max_length=255, default="none")
    award = models.CharField(max_length=255, default="none")
    ects_credits = models.CharField(max_length=255, default="0")
    mode = models.CharField(max_length=255, default="none")
    deadline = models.CharField(max_length=255, default="1/1/2022")
    start_date = models.CharField(max_length=255, default="1/1/2022")
    end_date = models.CharField(max_length=255, default="1/1/2023")
    nfq = models.CharField(max_length=255, default="0")
    ote_flag = models.CharField(max_length=255, default="none")
    link = models.CharField(max_length=255, default="none")
    skills = models.CharField(max_length=255, default="none")
    delivery = models.CharField(max_length=255, default="none")



    def __str__(self):
        return self.title









