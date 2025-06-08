# hexlet_django_blog/article/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    data = {"message": "article", "type": "demo"}
    return JsonResponse(data)
