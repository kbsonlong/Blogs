# coding:utf8
from __future__ import unicode_literals

from django.db import models

from DjangoUeditor.models import UEditorField
from datetime import datetime

# Create your models here.
class Catagory(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称',max_length=30)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称',max_length=16)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    #content = models.TextField('博客正文')
    # 仅修改 content 字段
    content = UEditorField('博客正文', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    created_time = models.DateTimeField('发布时间',auto_now_add=True)
    # updated_time = models.DateTimeField('最后更新时间', auto_now_add=True, default=datetime.now())
    catagory = models.ForeignKey(Catagory,verbose_name='分类')
    tags = models.ManyToManyField(Tag,verbose_name='标签')

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog,verbose_name='博客')
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=240)
    created = models.DateTimeField('发布时间',auto_now_add=True)

    def __unicode__(self):
        return self.content