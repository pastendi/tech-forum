from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    latest_post = Post.objects.all().order_by(
        "-date")[:6]  # three most recent post
    return render(request, 'blog/index.html', {'posts': latest_post})


def all_posts(request):
    posts = Post.objects.all().order_by(
        "-date")
    return render(request, 'blog/all-posts.html', {'posts': posts})


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/single-post.html', {'post': post,
                                                     'tags': post.tags.all()})
