"""isur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from articles.views import *
from isur import settings

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^fixtures/(?P<name>\w+)$', fixtures, name='fixtures'),
    url(r'^$', main, name='main'),
    url(r'^about-us/$', main, name='about'),
    url(r'^activities/$', our_activities, name='activities'),
    url(r'^concepts/$', mainconcepts, name='concepts'),
    url(r'^news/$', news, name='news'),
    url(r'^news/get/(?P<pk>[0-9]+)$', get_news, name='get_news'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^blog/get/(?P<pk>[0-9]+)$', get_blog, name='get_blog'),
    url(r'^history/$', history, name='history'),
    url(r'^history/get/(?P<pk>[0-9]+)$', get_history, name='get_history'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^publications/$', main, name='publications'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns()
