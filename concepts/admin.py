from django.contrib import admin
from .models import *
from modeltranslation.admin import TabbedTranslationAdmin
import concepts.translation


# Register your models here.

class MainConceptsAdmin(TabbedTranslationAdmin):
    list_display = ('title',)
    fields = ('bio', 'bio_image', 'climate_image', 'climate', 'development_image', 'development', 'slow_food_image', 'slow_food_text')


admin.site.register(MainConcepts, MainConceptsAdmin)
