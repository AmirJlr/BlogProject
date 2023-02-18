from django.shortcuts import render
from .models import Category, Post
# Create your views here.

def list_view(request):
    posts = Post.objects.all()

