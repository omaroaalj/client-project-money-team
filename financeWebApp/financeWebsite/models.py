from django.db import models
from django.db.models.functions import Now

# Create your models here.


class ContactEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    date = models.DateTimeField(db_default=Now())

    def __str__(self):
        return self.name + " (" + str(self.date) + ")"

    class Meta:
        verbose_name_plural = "Contact Entries"
