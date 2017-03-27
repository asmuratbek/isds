# coding=utf-8
import datetime
import random
import threading

from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader

from about.models import *
from articles.models import *
from concepts.models import *
from emails.models import *
from partners.models import *
from social.views import *


# Create your views here.
def main(request):
    _news = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Новости')).distinct().order_by(
        '-date')[:3]
    _blog = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Блог')).distinct().order_by('-date')[
            :3]
    history = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Истории')).distinct().order_by(
        '-date')[:3]

    reformed_news = format_news_grid(_news)

    photo_slide = Sliders.objects.filter(
        category__in=Category.objects.filter(title_ru='Фото слайдер')).distinct()
    video_slide = Sliders.objects.filter(category__in=Category.objects.filter(title_ru='Видео слайдер')).distinct()
    main_slide = Sliders.objects.filter(category__in=Category.objects.filter(title_ru='Главныйс')).distinct()
    partners = Partners.objects.all()
    contact = Contacts.objects.first()

    params = {
        'reformed_news': reformed_news,
        'blog': _blog,
        'history': history,
        'publications': publications,
        'photo_slider': photo_slide,
        'video_slider': video_slide,
        'main_slider': main_slide,
        'partners': partners,
        'contact': contact,
    }

    params.update(social(request))

    # print reformed_news
    # return JsonResponse(dict(objects=reformed_news))
    return render(request, 'main/index.html', params)


def fixtures(request, name):
    if name == 'news':
        for i in range(0, 21):
            post = Articles()
            post.title = 'Новость ' + str(random.randrange(1000, 9999))
            post.text = 'lorem ipsum dolor sit amet'
            post.date = datetime.date.today()
            post.article_id = 1
            post.image = 'images/sliders/news_image.png'
            post.save()

        return JsonResponse(dict(success=True, message='Heeey!'))


def news(request):
    _news = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Новости')).distinct().order_by(
        '-date')

    reformed_news = format_news_grid(_news)
    paginator = Paginator(reformed_news, 6)
    page = request.GET.get('page', 1)
    pages = paginator.page(page)

    params = {
        'reformed_news': reformed_news,
        'news': _news,
        'pages': pages
    }

    params.update(social(request))
    params.update(contacts(request))
    return render(request, 'main/news.html', params)


def blog(request):
    _blog = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Блог')).distinct().order_by('-date')
    paginator = Paginator(_blog, 6)
    page = request.GET.get('page', 1)
    pages = paginator.page(page)

    params = {
        'blog': _blog,
        'pages': pages,
    }
    params.update(social(request))
    params.update(contacts(request))
    return render(request, 'main/blog.html', params)


def format_news_grid(objects):
    counter = 0
    result = list()
    for item in objects:
        counter += 1
        post = dict(
            id=item.id,
            title=item.title,
            text=item.text,
            image=item.image,
            date=item.date,
            article=item.article.title,
            class_name='col-md-3 col-sm-3 col-xs-12'
        )
        if counter is 1:
            post['class_name'] = 'col-md-6 col-sm-6 col-xs-12'

        if counter is 6:
            counter = 0
            post['class_name'] = 'col-md-6 col-sm-6 col-xs-12'

        result.append(post)
    return result


def get_blog(request, pk):
    article_blog = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Блог')).filter(id=pk).first()

    params = {

        'article_blog': article_blog,

    }

    params.update(social(request))
    params.update(contacts(request))
    return render(request, 'main/detail_news.html', params)


def get_news(request, pk):
    article_news = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Новости')).filter(
        id=pk).first()
    params = {
        'article_news': article_news,
    }
    params.update(social(request))
    params.update(contacts(request))
    return render(request, 'main/detail_news.html', params)


def get_history(request, pk):
    article_history = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Истории')).filter(
        id=pk).first()

    params = {
        'article_history': article_history
    }
    params.update(social(request))
    params.update(contacts(request))

    return render(request, 'main/detail_news.html', params)


def mainconcepts(request):
    concepts = MainConcepts.objects.get()

    params = {
        'concepts': concepts
    }
    params.update(social(request))
    params.update(contacts(request))
    return render(request, 'main/concepts.html', params)


def our_activities(request):
    local = Programms.objects.filter(
        category__in=Category.objects.filter(title_ru='МИПБ')).distinct()
    regional = Programms.objects.filter(
        category__in=Category.objects.filter(title_ru='РП')).distinct()
    main = Programms.objects.filter(
        category__in=Category.objects.filter(title_ru='ОМР')).distinct()
    results = Programms.objects.filter(
        category__in=Category.objects.filter(title_ru='ОР')).distinct()

    tourism = Tourism.objects.first()
    socialp = SocialProjects.objects.all()

    params = {
        'local': local,
        'regional': regional,
        'main': main,
        'results': results,
        'tourism': tourism,
        'socialp': socialp,
    }
    params.update(social(request))
    params.update(contacts(request))
    return render(request, 'main/our_activities.html', params)


def history(request):
    _history = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Истории')).distinct().order_by(
        '-date')
    paginator = Paginator(_history, 6)
    page = request.GET.get('page', 1)
    pages = paginator.page(page)

    params = {
        'history': _history,
        'pages': pages
    }

    params.update(social(request))
    params.update(contacts(request))
    return render(request, 'main/histories.html', params)


def gallery(request):
    _gallery = Sliders.objects.filter(category__in=Category.objects.filter(title_ru='Фото слайдер')).distinct()

    params = {
        'gallery': _gallery,
    }

    params.update(social(request))
    params.update(contacts(request))

    return render(request, 'main/gallery.html', params)


def contacts(request):
    contact = Contacts.objects.first()

    params = {
        'contact': contact
    }

    return params


def save_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = Emails(name=name, email=email)
        user.save()
    return HttpResponse("Вы успешно подписаны!")

def send_news_email(title, body, to):
    email = EmailMessage(title, body=body, to=to)
    email.content_subtype = 'html'
    email.send()


def send_email_in_thread(title, t, c, emails):
    content = t.render(c)
    send_news_email(title, body=content,
                    to=emails)


@receiver(post_save, sender=Articles)
def send_email(sender, instance, created, **kwargs):

    if instance.article.title == u'Новости':
        t = loader.get_template('email.html')
        emails = [i.email for i in Emails.objects.all()]
        c = dict(title=instance.title, text=instance.text, date=instance.date)
        if created:
            thread = threading.Thread(target=send_email_in_thread,
                                      args=(instance.title, t, c, emails))
            thread.start()


def about_page(request):
    about = AboutUs.objects.first()
    _partners = Partnerss.objects.all()
    params = {
        'about': about,
        'apartners': _partners,
    }

    params.update(social(request))
    params.update(contacts(request))

    return render(request, 'main/about_us.html', params)

def publications(request):
    publication = Publications.objects.all().order_by('-date')


    params = {
        'publication': publication,
    }

    return render(request, 'main/publications.html', params)