from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import User

from core.utils import content_file_name


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


class CourseModel(models.Model):

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









