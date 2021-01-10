from django.db import models


class User(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别", blank=True)
    password = models.CharField(max_length=128, verbose_name="密码")
    qq_name = models.CharField(max_length=128, verbose_name="QQ账号", blank=True)
    wc_name = models.CharField(max_length=128, verbose_name="微信账号", blank=True)
    phone = models.CharField(max_length=128, verbose_name="电话", blank=True)
    email = models.EmailField(verbose_name="Email", blank=True)
    signature = models.CharField(max_length=128, verbose_name="签名")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态", blank=True)
    created_time = models.DateField(auto_now_add=True, editable=False, verbose_name="创建时间", blank=True)

    def __str__(self):
        return '<User:{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "读者信息"


