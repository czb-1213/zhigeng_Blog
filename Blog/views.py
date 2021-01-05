from django.shortcuts import render
from Blog.models import Article


def archive(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def tosearch(request):
    return render(request, 'search.html')
