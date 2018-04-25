from django.db import models
from django.conf import settings
from django_mysql.models import JSONField

# Create your models here.

class Githubdata(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.CharField(max_length=20)
    data = models.CharField(max_length=100000)
    victim = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.service

