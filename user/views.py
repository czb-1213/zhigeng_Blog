from django.shortcuts import render

from .models import User
def info(request):
    useId = request.session['User_id']
    userInfo = UserInFo.objects.get(id=UserID)
    username = request.session['User_name']
    usersignature = request.session['User_signature']
    userphone = request.session['User_phone']
    userqq_name = request.session['User_qq_name']
    userwc_name = request.session['User_wc_name']
    content = {
        'title' : '个人信息',
        'User_name' : 'username',
        'User_signature' : 'usersignature',
        'User_phone': 'userphone',
        'User_qq_name' : 'userqq_name',
        'User_wc_name' : 'userwc_name'
    }
    return render(request,'ppage.html',content)