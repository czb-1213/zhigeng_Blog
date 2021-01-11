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
    return render(request, 'passage.html', {'sentdoc': sentdoc})


def myinfo(request):
    if request.session.get('is_login', False):
        id = request.session['user_id']
        context = {
            'send': models.Article.objects.filter(writer_id=id)
        }
        return render(request, 'ppage.html', context)
    else:
        return redirect('/login/')


def remove(request, id):
    if request.session.get('is_login', False):
        models.Article.objects.filter(id=id).delete()
        return redirect('/myinfo/')
    else:
        return redirect('/login/')


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


def addarticle(request):
    message='成功'
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        id = request.session['user_id']
        models.Article.objects.create(title=title, writer_id=id, content=content)
        return render(request, 'editor.html')
    except:
        message = '错误'


def articsent(request):
    sentdoc = models.Article.objects.order_by("-click_nums")[0:10]
    print(sentdoc)
    return render(request, "passage.html", {'sentdoc': sentdoc})
