from django.contrib import admin
from .models import *
# Register your models here.

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Partners,PartnersAdmin)