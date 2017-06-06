from modeltranslation.translator import translator, TranslationOptions

from .models import *


class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'pre_text',)


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

class LocalLeadTranslationOptions(TranslationOptions):
    fields = ('text',)

class ExpirienceChangeTranslationOptions(TranslationOptions):
    fields = ('text',)

class PublicationsTranslationOptions(TranslationOptions):
    fields = ('text',)

class LogoTranslationOptions(TranslationOptions):
    fields = ('image', )

class SliderMaskTranslationOptions(TranslationOptions):
    fields = ('image', )

translator.register(Category, CategoryTranslationOptions)
translator.register(Articles, ArticlesTranslationOptions)
translator.register(Sliders, SlidersTranslationOptions)
translator.register(Contacts, ContactsTranslationOptions)
translator.register(SocialProjects, SocialProjectsTranslationOptions)
translator.register(Programms, ProgrammsTranslationOptions)
translator.register(Tourism, TourismTranslationOptions)
translator.register(Publications, PublicationsTranslationOptions)
translator.register(Logo, LogoTranslationOptions)
translator.register(SliderMask, SliderMaskTranslationOptions)
translator.register(LocalLead, LocalLeadTranslationOptions)
translator.register(ExpirienceChange, ExpirienceChangeTranslationOptions)
