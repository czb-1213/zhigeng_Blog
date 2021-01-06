from idlelib.multicall import r

from django.shortcuts import render, get_object_or_404
from Blog.models import Article


def archive(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def tosearch(request):
    return render(request, 'search.html')
def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    # total_views：记录文章访问量
    # 一般通过“对象类型：对象ID：对象属性”来命名一个键
    total_views = r.incr("article:{}:views".format(article.id))
    # zincrby的原型是zincrby(name,amount,value):根据amount所设定的步长值增加有序集合（name）中的value的数值
    # 实现了article_ranking中的article.id以步长1自增，
    # 即文章访问一次，article_ranking就将文章id的值增1
    r.zincrby('article_ranking', 1,article.id)
    # 得到article_ranking中排序前10名对象
    article_ranking = r.zrange('article_ranking', 0, -1, desc=True)[:10]
    print(article_ranking)
    # 得到前10名文章ID
    article_ranking_ids = [int(id) for id in article_ranking]
    print(article_ranking_ids)
    # 查询出id在article_ranking_ids这个范围内的所有文章对象，并以文章对象为元素生成列表
    most_viewed = list(Article.objects.filter(id__in=article_ranking_ids))
    print(most_viewed)
    # 对所得到的列表进行排序
    most_viewed.sort(key=lambda x: article_ranking_ids.index(x.id))

    # 将访问次数传递给模板，将最受欢迎文章列表传递给前端
    return render(request, "index.html",
                  {"article": article, "total_views": total_views,"most_viewed": most_viewed})