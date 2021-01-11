from django.shortcuts import render, redirect

from Blog import models
from .models import User


def info(request):
    username = request.session['User_name']
    usersignature = request.session['User_signature']
    userphone = request.session['User_phone']
    userqq_name = request.session['qq_name']
    userwc_name = request.session['wc_name']
    content = {
        'title': '个人信息',
        'User_name': username,
        'User_signature': usersignature,
        'User_phone': userphone,
        'User_qq_name': userqq_name,
        'User_wc_name': userwc_name
    }
    return render(request, 'ppage.html', content)


def mysend(request):
    if request.session.get('is_login', False):
        id = request.session['user_id']
        context = {
            'send': models.Article.objects.filter(writer_id=id)
        }
        return render(request, 'ppage.html', context)
    else:
        return redirect('/login/')


def mynotice(request):
    if request.session.get('is_login', False):
        return render(request, 'myinfo.html')
    else:
        return redirect('/login/')

def mypoint(request):
    if request.session.get('is_login', False):
        return render(request, 'mypoint.html')
    else:
        return redirect('/login/')

