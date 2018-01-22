# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response

# Create your views here.
from blog.models import *
from blog.forms import CommentForm
from django.http import Http404
import markdown

md = markdown.Markdown(extensions=['codehilite'])

def test(request):
    blogs = Blog.objects.all().order_by('-created_time')
    return render_to_response('sss.html',{'blogs':blogs})

def index(request):
    blogs = Blog.objects.all().order_by('-created_time')
    return render_to_response('index.html',{'blogs':blogs})

def about(request):

    return render_to_response('about.html',{'blogs':''})


def listpic(request):

    return render_to_response('listpic.html',{'blogs':''})

def newslistpic(request):

    return render_to_response('newslistpic.html',{'blogs':''})




def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created_time')
    return render_to_response('blog/blog_list.html',{'blogs':blogs})

def get_details(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created_time'),
        'form':form
    }
    # return render(request,'blog/blog_details.html',ctx)
    return render(request,'blog_content.html',ctx)


def post_content(request,blog_id):
    try:
        blog = Blog.objects.get(id = blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        blog.title = request.POST.get('blog_title')
        blog.content = request.POST.get('blog_content')
        blog.save()
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created_time'),
    }
    return render(request, 'blog/blog_details.html', ctx)



