from django.contrib import admin

from articles.models import Programms, SocialProjects, Tourism
from .models import *
from modeltranslation.admin import TabbedTranslationAdmin
import about.translation

class AboutUSInline(admin.StackedInline):
    model = Partners
    extra = 3
# Register your models here.

class AboutUsAdmin(TabbedTranslationAdmin):
    list_display = ('title',)
    inlines = [AboutUSInline]


class PartnersAdmin(TabbedTranslationAdmin):
    list_display = ('title',)

class ProgrammsAdmin(TabbedTranslationAdmin):
    list_display = ('text',)

class TourismAdmin(TabbedTranslationAdmin):
    list_display = ('text',)

class SocialProjectsAdmin(TabbedTranslationAdmin):
    list_display = ('text',)

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Partners, PartnersAdmin)

