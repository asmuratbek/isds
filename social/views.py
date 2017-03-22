from django.shortcuts import render

from social.models import *


# Create your views here.

def social(request):
    _social = SocialLinks.objects.get()
    params = {
        'socials': _social
    }
    return params
