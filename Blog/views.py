from django.shortcuts import render
from Blog.models import Article


def archive(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts': posts})