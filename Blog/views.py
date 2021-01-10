from idlelib.multicall import r

from django.shortcuts import render, get_object_or_404
from Blog.models import Article

from zhigeng_Blog.Blog import models


def archive(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def tosearch(request):
    return render(request, 'search.html')
def articlecont(request):
     nid = request.GET.get('nid')
     articledata = models.Article.objects.filter(id=nid).first()
     models.Article.increase_click_nums(articledata)
     hotdoc = models.Article.objects.order_by("-click_nums")[0:10]
     return render(request, "index.html", {"articledata": articledata,'hotdoc':hotdoc})


def articsent(request):
    mid = request.GET.get('mid')
    articledate = models.Article.objects.filter(id=mid).first()
    models.Article.increase_click_nums(articledate)
    sentdoc = models.Article.objects.order_by("-click_nums")[0:10]
    return render(request, "passage.html", {"articledate": articledate, 'sentdoc': sentdoc})