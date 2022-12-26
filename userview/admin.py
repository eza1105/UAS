
from django.db import models
from django.contrib import admin
from .models import *


class Fax(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()


