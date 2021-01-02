from django.http import request
from django.shortcuts import render


# Create your views here.
def register(request):
    context = {

    }
    return render(request, 'register.html', context)
