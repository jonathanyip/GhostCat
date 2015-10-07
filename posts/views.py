from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from users.models import UserProfile

def homepage(request):
    latest_posts = Post.objects.all().order_by('-post_date')[:5]
    
    # Checks whether we're already following this person
    if request.user.is_authenticated():
        for post in latest_posts:
            post.is_following = request.user.userprofile.following.filter(pk=post.post_author.pk)
    context = { 'latest_posts': latest_posts }
    return render(request, 'homepage.html', context)

def following(request):
    if not request.user.is_authenticated():
        redirect('Homepage')
    
    # This next line is pure magic...
    # How does it even know what to do?
    posts = Post.objects.filter(post_author=request.user.userprofile.following.all()).order_by('-post_date')[:20]
    
    for post in posts:
        post.is_following = True
    context = { 'header': 'People you follow',  'posts': posts }
    
    return render(request, 'postPage.html', context)

def postLink(request, postLinkPk):
    post = Post.objects.get(pk=postLinkPk)
    if request.user.is_authenticated():
        post.is_following = request.user.userprofile.following.filter(pk=post.post_author.pk)
    
    context = { 'posts': {post} }
    
    return render(request, 'postPage.html', context)