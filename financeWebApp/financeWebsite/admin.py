from django.contrib import admin
from .models import ContactEntry


# Register your models here.
class ContactEntryAdmin(admin.ModelAdmin):
    list_display = ["name", "date"]

# Current Client database / newly added clients


admin.site.register(ContactEntry, ContactEntryAdmin)
