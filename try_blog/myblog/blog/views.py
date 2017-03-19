from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.
def index(request):
    articles = Article.objects.all()
    print (request.GET)
    return render(request, 'blog/index.html',{'articles': articles})


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    print (article)
    return render(request, 'blog/article_page.html',{'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html', {'article': {'title': '', 'content': ''}})
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article':article})

@csrf_exempt
def edit_action(request):
    titless = request.POST.get('title', 'TITLE')
    contentss = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    #forms.py   throw
    print (titless, contentss)
    if article_id == '0':
        b = Article(title=titless, content=contentss)#models.Article.objects.create(title=titless , content=contentss)
        b.save()#article = models.Article.objects.all()
        return HttpResponseRedirect('/blog/index')#return render(request, 'blog/index.html',{'articles': articles})

    article = Article.objects.get(pk=article_id)
    article.title = titless
    article.content = contentss
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})