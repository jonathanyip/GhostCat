from django.contrib.auth import authenticate, login, logout
from django.utils.html import escape
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Post
from .models import UserProfile

# Handle Logins and Registers (the pages and POST requests)
def userLogin(request):
	if request.user.is_authenticated():
		return redirect('Homepage')
	
	# Do logins
	if 'form-login-username' in request.POST and 'form-login-password' in request.POST:
		username = escape(request.POST['form-login-username'])
		password = escape(request.POST['form-login-password'])
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('Homepage')
			else:
				context = { 'login_error': 'Woah! Cannot log you in!<br>Your account seems to be disabled.' }
				return render(request, 'login.html', context)
		else:
			context = { 'login_error': 'Woah! Cannot log you in!<br>Check your password/username.' }
			return render(request, 'login.html', context)
	
	# Do registers
	if 'form-register-email' in request.POST and 'form-register-username' in request.POST and 'form-register-password' in request.POST:
		email = escape(request.POST['form-register-email'])
		username = escape(request.POST['form-register-username'])
		password = escape(request.POST['form-register-password'])
		if not User.objects.filter(email = email).exists() and not User.objects.filter(username = username).exists():
			user = User.objects.create_user(username=username, email=email, password=password)
			
			u = UserProfile(user=user)
			u.save()
			
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('Homepage')
		else:
			context = { 'register_error': 'Woah! This username/email combo exists already!' }
			return render(request, 'login.html', context)
	
	# No POST, so just show the normal page
	return render(request, 'login.html')

# Logs out a user
def userLogout(request):
	logout(request)
	return redirect('Homepage')

# Handles a follow request
def userFollow(request, userpk):
	if not request.user.is_authenticated():
		return redirect('Login')
	
	otherUser = User.objects.get(pk=userpk)
	thisUser = request.user.userprofile
	if not thisUser.following.filter(pk=userpk):
		thisUser.following.add(otherUser)
		thisUser.save()
	
	return redirect('Following')

# Handles an unfollow request
def userUnfollow(request, userpk):
	if not request.user.is_authenticated():
		return redirect('Login')
	otherUser = User.objects.get(pk=userpk)
	thisUser = request.user.userprofile
	if thisUser.following.filter(pk=userpk):
		thisUser.following.remove(otherUser)
	thisUser.save()
	
	return redirect('Following')

# Handles the posting form
def userPost(request):
	if not request.user.is_authenticated():
		return redirect('Login')
	
	if 'form-post' in request.POST:
		text = request.POST['form-post']
		if(len(text) > 140):
			context = { 'post_error': 'The post needs to be 140 characters or less!' }
			return render(request, 'post_form.html', context)
		post = Post(post_text=text, post_author=request.user)
		post.save()
		return redirect('Homepage')
	
	return render(request, 'postForm.html')