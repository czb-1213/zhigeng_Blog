# Generated by Django 3.1.4 on 2021-01-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hot',
            field=models.IntegerField(choices=[(1, '是'), (2, '否')], default=2, verbose_name='热搜榜'),
        ),
    ]
