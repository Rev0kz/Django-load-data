from django.db import models
from postgres_copy import CopyManager


class visitors(models.Model):

  name = models.CharField(max_length=80, verbose_name="Name")
  location = models.CharField(max_length=80, verbose_name="Name")
  country =  models.CharField(max_length=80, verbose_name="Name")
  email = models.CharField(max_length=80, verbose_name="Name")
  objects = CopyManager()
