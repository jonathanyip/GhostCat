from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def homepage(request):
    latest_posts = Post.objects.all().order_by('-post_date')[:5]
    context = { 'latest_posts': latest_posts }
    return render(request, 'homepage.html', context)

def following(request):
    return HttpResponse("Following")