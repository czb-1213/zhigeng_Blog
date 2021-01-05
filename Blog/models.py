from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='文章类别')
    number = models.IntegerField(default=1, verbose_name='分类数目')


class Tags(models.Model):
    name = models.CharField(max_length=20, verbose_name='文章标签')
    number = models.IntegerField(default=1, verbose_name='标签数目')


class Article(models.Model):
    HOT_ITEMS = [
        (1, '是'),
        (2, '否'),
    ]
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(default='', verbose_name='正文')
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    click_nums = models.IntegerField(default=0, verbose_name='点击量')
    hot = models.IntegerField(default=0,choices=HOT_ITEMS, verbose_name="热搜榜")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章类别')
    tags = models.ManyToManyField(Tags, verbose_name='文章标签')

