from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
