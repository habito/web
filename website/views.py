from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from user_profile.forms import *


def index(request):
    return render(request, 'website/index.html', {})

def browse(request):
    return render(request, 'website/browse.html', {})

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
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

def login_user(request):
	context = RequestContext(request)
	
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(user=user, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				state = "You're logged in to Mauraders!"
			else:
				state = "Your account is not active, please contact us."
		else:
			state = "Your username and/or password were incorrect, please try again."
	return render_to_response(
			'website/login.html', 
			{}, context)
	
				
