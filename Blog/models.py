from django.db import models
from user.models import User


# Create your models here.

class Article(models.Model):
    HOT_ITEMS = [
        (1, '是'),
        (2, '否'),
    ]
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(default='', verbose_name='正文')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    click_nums = models.IntegerField(default=0, verbose_name='点击量')
    hot = models.IntegerField(default=2, choices=HOT_ITEMS, verbose_name="热搜榜")

    def increase_views(self):
        self.click_nums += 1
        self.save(update_fields=['click_nums'])
