from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import *


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
    list_display = ('text_html',)


class TourismAdmin(TabbedTranslationAdmin):
    list_display = ('text_html',)


class SocialProjectsAdmin(TabbedTranslationAdmin):
    list_display = ('text_html',)


class PublicationsAdmin(TabbedTranslationAdmin):
    fields = ('title', 'image', 'text', )
    list_display = ('title', 'text', )


class LogoAdmin(TabbedTranslationAdmin):
    fields = ('image',)
    list_display = ('title',)

class SliderMaskAdmin(TabbedTranslationAdmin):
    fields = ('image',)
    list_display = ('title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sliders, SlidersAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Programms, ProgrammsAdmin)
admin.site.register(SocialProjects, SocialProjectsAdmin)
admin.site.register(Tourism, TourismAdmin)
admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(SliderMask, SliderMaskAdmin)
