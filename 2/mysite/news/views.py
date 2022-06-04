from django.shortcuts import render

from .models import News


def index(request):
    author = "allelleo"
    news = News.objects.all()

    context = {
                'news': news,
               'author': author,
               'title': 'Список Новостей'
               }
    return render(request=request, template_name='news/index.html', context=context)
