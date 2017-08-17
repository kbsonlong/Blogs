#coding:utf-8

from django.conf.urls import url,include
from blog.views import *
urlpatterns = [
    url(r'^blogs/$',get_blogs),
    url(r'^test/$',test),
    url(r'^index/$',index),
    url(r'^about/$',about),
    url(r'^newslistpic/$',newslistpic),
    url(r'^listpic/$',listpic),
    url(r'^detail/(\d+)/$',get_details ,name='blog_get_detail'),
]