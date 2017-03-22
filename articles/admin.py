from django.contrib import admin
from .models import *
from modeltranslation.admin import TabbedTranslationAdmin
import articles.translation


# Register your models here.

class ArticlesAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class SlidersAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'category')

class ContactsAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'phone', 'email', 'address')
    fields = ('phone', 'email', 'address')

class ProgrammsAdmin(TabbedTranslationAdmin):
    list_display = ('text',)

class TourismAdmin(TabbedTranslationAdmin):
    list_display = ('text',)

class SocialProjectsAdmin(TabbedTranslationAdmin):
    list_display = ('text',)

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sliders, SlidersAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Programms, ProgrammsAdmin)
admin.site.register(SocialProjects, SocialProjectsAdmin)
admin.site.register(Tourism, TourismAdmin)
