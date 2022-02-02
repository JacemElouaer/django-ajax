from django.shortcuts import render
from django.http  import JsonResponse
from .models import *
# Create your views here.


def index(request):
    return render(request,  'pages/index.html')

def getComments(request):
    comments =  Comment.objects.all()
    return  JsonResponse({"comments" :  list(comments)})