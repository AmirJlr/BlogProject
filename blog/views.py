from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Category, Post


# Create your views here.

def list_view(request):
    posts = Post.objects.filter(status=Post.StatusChoices.PUBLISHED, publish_time__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/list.html', context)


# list objects with Class Base View
class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.StatusChoices.PUBLISHED, publish_time__lte=timezone.now())
    template_name = 'blog/list.html'
    context_object_name = 'posts'


def detail_view(request, year, month, day, slug):
    post = get_object_or_404(Post, publish_time__year=year, publish_time__month=month, publish_time__day=day, slug=slug)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


# detail view with CBV
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'

    def get_object(self, queryset=None):
        return Post.objects.get(publish_time__year=self.kwargs['year'],
                                publish_time__month=self.kwargs['month'],
                                publish_time__day=self.kwargs['day'],
                                slug=self.kwargs['slug'])
