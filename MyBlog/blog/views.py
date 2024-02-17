from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
  

def post_list_with_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list(request):
    return render(request, 'index.html')

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'posts_by_author.html', {'author': author, 'posts': posts})

