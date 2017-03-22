from modeltranslation.translator import translator, TranslationOptions
from .models import *


class MainConceptsTranslationOptions(TranslationOptions):
    fields = ('bio', 'climate', 'development', 'slow_food_text')


translator.register(MainConcepts, MainConceptsTranslationOptions)
