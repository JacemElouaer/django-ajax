from django.shortcuts import render
from django.http import JsonResponse
from .models import *


# Create your views here.


def index(request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request, 'pages/index.html', context)


def getComments(request):
    comments = Comment.objects.all()
    return JsonResponse({"comments": list(comments)})
