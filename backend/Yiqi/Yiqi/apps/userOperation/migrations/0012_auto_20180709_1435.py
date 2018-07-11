# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-09 14:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messagess', '0001_initial'),
        ('activity', '0026_auto_20180709_1435'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userOperation', '0011_auto_20180709_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=50, verbose_name='消息标题')),
                ('content', models.TextField(default='消息内容')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='消息时间')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityModel', verbose_name='活动')),
                ('sysuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messagess.SysUserModel', verbose_name='系统用户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='接收用户')),
            ],
            options={
                'verbose_name': '消息内容管理',
                'verbose_name_plural': '消息内容管理',
            },
        ),
        migrations.AlterModelOptions(
            name='commentsmodels',
            options={'verbose_name': '用户评论记录', 'verbose_name_plural': '用户评论记录'},
        ),
        migrations.AlterField(
            model_name='feedbackmodels',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='FeedBackModels/%y/%d/be9c78ce0ae041609f7f3000e36762bf', verbose_name='反馈图片'),
        ),
    ]