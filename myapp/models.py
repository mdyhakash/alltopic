from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    c_title = models.CharField(max_length=200)
    c_code = models.CharField(max_length=20)
    c_teacher = models.CharField(max_length=100)
    s_mid= models.TextField()
    s_final= models.TextField()
    c_description = models.TextField()
    c_link = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.c_title