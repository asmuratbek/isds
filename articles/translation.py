from modeltranslation.translator import translator, TranslationOptions
from .models import *


class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class SlidersTranslationOptions(TranslationOptions):
    fields = ('title',)


class ContactsTranslationOptions(TranslationOptions):
    fields = ('address',)

class SocialProjectsTranslationOptions(TranslationOptions):
    fields = ('text',)

class ProgrammsTranslationOptions(TranslationOptions):
    fields = ('text',)

class TourismTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Articles, ArticlesTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Sliders, SlidersTranslationOptions)
translator.register(Contacts, ContactsTranslationOptions)
translator.register(SocialProjects, SocialProjectsTranslationOptions)
translator.register(Programms, ProgrammsTranslationOptions)
translator.register(Tourism, TourismTranslationOptions)
