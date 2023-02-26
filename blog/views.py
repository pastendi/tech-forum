from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def all_posts(request):
    pass  # passes the function with nothing


def single_post(request):
    pass
