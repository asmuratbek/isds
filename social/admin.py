from django.contrib import admin
from .models import *


# Register your models here.

class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'f_link', 't_link', 'i_link', 'y_link')
    fields = ['f_link', 't_link', 'i_link', 'y_link']

admin.site.register(SocialLinks, SocialLinksAdmin)
