from django.shortcuts import render
from .models import Category, Post


# Create your views here.

def list_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/list.html', context)


def detail_view(request, slug):
    # post = Post.objects.get(pk=pk)
    # context = {'post': post}
    return render(request, 'blog/detail.html')
