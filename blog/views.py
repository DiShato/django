from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Post


# Create your views here.

def article_list(request):
    articles = Post.objects.all()  
    # return render (request, template_name='blog/post_list.html', context={'article':articles})
    return render (request, template_name='blog/post_list.html', context={'articles': articles, 'title': Post.title, 'content': Post.content, 'created_at': Post.created_at})
