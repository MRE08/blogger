from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.conf import settings
# Create your views here.

#Creating a view for home page
def index(request):
    #Get all objects in the Post Model
    posts = Post.objects.all()
    #Passing all the files(static files) in the media url
    context = {
        'posts':posts, 'media_url':settings.MEDIA_URL
    }
    return render(request, 'blog/index.html', context)