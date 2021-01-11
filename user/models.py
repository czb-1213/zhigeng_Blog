from django.db import models


class User(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别", blank=True, default='男')
    password = models.CharField(max_length=128, verbose_name="密码")
    qq_name = models.CharField(max_length=128, verbose_name="QQ账号", blank=True, default='null')
    wc_name = models.CharField(max_length=128, verbose_name="微信账号", blank=True, default='null')
    phone = models.CharField(max_length=128, verbose_name="电话", blank=True, default='null')
    email = models.EmailField(verbose_name="Email", blank=True, default='null')
    signature = models.CharField(max_length=128, verbose_name="签名", default='null')
    created_time = models.DateField(auto_now_add=True, editable=False, verbose_name="创建时间", blank=True)

    def __str__(self):
        return '<User:{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "读者信息"


