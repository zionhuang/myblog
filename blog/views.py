from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article.html', {'article': article})


def edit(request, article_id):
    if '0' == str(article_id):
        return render(request, 'blog/edit.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit.html', {'article': article})


def create(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    article_id = request.POST.get('article_id', '0')

    if '0' == article_id:
        models.Article.objects.create(title=title, content=content)
        return HttpResponseRedirect('/blog/index')
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return HttpResponseRedirect('/blog/index')
