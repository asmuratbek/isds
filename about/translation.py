from modeltranslation.translator import translator, TranslationOptions
from .models import *


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'our_see', 'mission', 'target1_text', 'target2_text')


class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(Partners, PartnersTranslationOptions)
