from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from user_profile.forms import *


def index(request):
    return render(request, 'website/index.html', {'request':request})

def browse(request):
    return render(request, 'website/browse.html', {'request':request})

def register(request):
	context = RequestContext(request)
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)	
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()	
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			
			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']
			
			profile.save()
			registered = True
		
		else:
			print (user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	
	return render_to_response(
            'website/sign_up.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'request':request}, context)

def login_user(request):
	context = RequestContext(request)
	if request.POST:
<<<<<<< HEAD
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(user=username, password=password)
=======
		print('hello')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user)
>>>>>>> 9036211641b1f06e866dda637295dcb91d59265d
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/me')
		else:
			state = "Your username and/or password were incorrect, please try again."
			print(state)
	return render_to_response(
			'website/login.html', 
			{'request':request}, context)

@login_required
def me(request):
	return render(request, 'website/me.html', {'request':request})
	
				
