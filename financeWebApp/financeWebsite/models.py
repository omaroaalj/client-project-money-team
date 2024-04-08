from django.db import models

# Create your models here.

class ContactEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    