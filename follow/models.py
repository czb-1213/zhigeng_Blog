from django.db import models

# Create your models here.
from user.models import User


class Fans(models.Model):
    fans_name = models.CharField(max_length=128, verbose_name="姓名")
    email = models.EmailField(verbose_name="Email")
    user = models.ManyToManyField(User, through='Follow')

    def __str__(self):
        return '<User:{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "粉丝信息"


class Follow(models.Model):
    fans = models.ForeignKey(Fans, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_time = models.DateField(auto_now_add=True, editable=False, verbose_name="关注时间")
