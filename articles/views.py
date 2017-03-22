# coding=utf-8
import datetime
import random

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from partners.models import *
from articles.models import *
from concepts.models import *
from social.views import *


# Create your views here.
def main(request):
    _news = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Новости')).distinct().order_by(
        '-date')[:3]
    _blog = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Блог')).distinct().order_by('-date')[
           :3]
    history = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Истории')).distinct().order_by(
        '-date')[:3]
    publications = Articles.objects.filter(
        article__in=Category.objects.filter(title_ru='Публикации')).distinct().order_by('-date')
    contacts = Contacts.objects.all()
    reformed_news = format_news_grid(_news)

    photo_slide = Sliders.objects.filter(
        category__in=Category.objects.filter(title_ru='Фото слайдер')).distinct()
    video_slide = Sliders.objects.filter(category__in=Category.objects.filter(title_ru='Видео слайдер')).distinct()
    main_slide = Sliders.objects.filter(category__in=Category.objects.filter(title_ru='Главныйс')).distinct()
    partners = Partners.objects.all()

    params = {
        'reformed_news': reformed_news,
        'blog': _blog,
        'history': history,
        'contact': contacts,
        'publications': publications,
        'photo_slider': photo_slide,
        'video_slider': video_slide,
        'main_slider': main_slide,
        'partners':partners,
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
    return render(request, 'main/detail_news.html', params)


def get_news(request, pk):
    article_news = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Новости')).filter(
        id=pk).first()
    params = {
        'article_news': article_news,
    }
    params.update(social(request))
    return render(request, 'main/detail_news.html', params)


def get_history(request, pk):
    article_history = Articles.objects.filter(article__in=Category.objects.filter(title_ru='Истории')).filter(
        id=pk).first()

    params = {
        'article_history': article_history
    }
    params.update(social(request))
    print article_history
    return render(request, 'main/detail_news.html', params)


def mainconcepts(request):
    concepts = MainConcepts.objects.get()

    params = {
        'concepts': concepts
    }
    params.update(social(request))
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

    tourism = Tourism.objects.get()
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
    return render(request, 'main/histories.html', params)

def gallery(request):
    _gallery = Sliders.objects.filter(category__in=Category.objects.filter(title_ru='Видео слайдер')).distinct()

    params = {
        'gallery': _gallery,
    }

    params.update(social(request))

    return render(request, 'main/gallery.html', params)