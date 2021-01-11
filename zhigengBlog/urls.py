"""zhigengBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from Login import views as Loginviews
from Blog import views as Blogviews
from user import views as Userviews

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.index),
    # url(r'^login/', views.login),
    # url(r'^register/', views.register),
    # url(r'^logout/', views.logout),
    path('', Loginviews.index),
    path('index/', Loginviews.index),
    path('admin/', admin.site.urls),
    path('write/', Loginviews.write),
    path('login/', Loginviews.login),
    path('toregister/', Loginviews.toregister),
    path('register/', Loginviews.register),
    path('logout/', Loginviews.logout),
    path('about/', Blogviews.about),
    path('tosearch/', Blogviews.tosearch),
    path('toimg/', Blogviews.toimg),
    path('toarticle/', Blogviews.toarticle),
    path('myinfo/', Blogviews.myinfo),
    path('articsent/', Blogviews.articsent),
    path('<int:id>/', Blogviews.article),
    path('mysend/', Userviews.mysend),

]
