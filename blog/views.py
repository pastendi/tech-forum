from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Blog app')


def all_posts(request):
    pass  # passes the function with nothing


def single_post(request):
    pass
