# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'index.html', {'post_list' : post_list})
def mark(request):
    return render(request, 'mark.html')
# def home(request):
#     post_list = Article.objects.all()  #获取全部的Article对象
#     return render(request, 'index.html')
# def home(request):
#     post_list = Article.objects.all()  #获取全部的Article对象
#     return render(request, 'index.html')
# def home(request):
#     post_list = Article.objects.all()  #获取全部的Article对象
#     return render(request, 'index.html')
# def home(request):
#     post_list = Article.objects.all()  #获取全部的Article对象
#     return render(request, 'index.html')
# def home(request):
#     post_list = Article.objects.all()  #获取全部的Article对象
#     return render(request, 'index.html')

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404

    return render(request,'post.html',{'post':post})
# Create your views here.
