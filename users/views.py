from django.contrib.auth import authenticate, login, logout
from django.utils.html import escape
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Post

def userLogin(request):
	if request.user.is_authenticated():
		return redirect('Homepage')
	
	# Handle Logins
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
	
	# Handle Registers
	if 'form-register-email' in request.POST and 'form-register-username' in request.POST and 'form-register-password' in request.POST:
		email = escape(request.POST['form-register-email'])
		username = escape(request.POST['form-register-username'])
		password = escape(request.POST['form-register-password'])
		if not User.objects.filter(email = email).exists() and not User.objects.filter(username = username).exists():
			user = User.objects.create_user(username=username, email=email, password=password)
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('Homepage')
		else:
			context = { 'register_error': 'Woah! This username/email combo exists already!' }
			return render(request, 'login.html', context)
	
	return render(request, 'login.html')

def userLogout(request):
	logout(request)
	return redirect('Homepage')

def userFollow(request, username):
	return HttpResponse("Follow")

def userPost(request):
	if not request.user.is_authenticated():
		return redirect('Login')
	
	if 'form-post' in request.POST:
		text = escape(request.POST['form-post'])
		if(len(text) > 140):
			context = { 'post_error': 'The post needs to be 140 characters or less!' }
			return render(request, 'post_form.html', context)
		post = Post(post_text=text, post_author=request.user)
		post.save()
		return redirect('Homepage')
		
	return render(request, 'post_form.html')