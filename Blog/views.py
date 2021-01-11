from idlelib.multicall import r

from django.shortcuts import render, get_object_or_404, redirect
from Blog.models import Article

from Blog import models


def archive(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def toimg(request):
    return render(request, 'images.html')


def toarticle(request):
    sentdoc = models.Article.objects.order_by("-click_nums")[0:10]
    return render(request, 'passage.html',{{'sentdoc':sentdoc}})


def myinfo(request):
    return render(request, 'myinfo.html')


def tosearch(request):
    return render(request, 'search.html')


def article(request, id):
    content = models.Article.objects.get(id=id)
    return render(request, 'passageContent.html', {'content': content})


def toart(request):
    return render(request, 'passageContent.html')


def hotarticle():
    hotdoc = models.Article.objects.order_by("-click_nums")[0:10]
    return hotdoc


def articsent(request):
    sentdoc = models.Article.objects.order_by("-click_nums")[0:10]
    print(sentdoc)
    return render(request, "passage.html", {'sentdoc': sentdoc})
