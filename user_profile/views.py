from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from user_profile.forms import *
from user_profile.models import UserProfile
from user_profile.models import * 
from django.forms import *

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
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(user=username, password=password)
		
		print('hello')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user)
		
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
	user = request.user
	up = UserProfile.objects.get(user=user)
	profile_pic_form = ProfilePicChangeForm()
	document_form = DocumentUploadForm()

	if request.method == 'POST':
		if 'document' in request.FILES:
			document_form = DocumentUploadForm(request.POST, request.FILES)
			if document_form.is_valid():
				up.document = request.FILES['document']
				up.save()
		elif request.POST.get('name', False) == 'email':
			user.email = request.POST['value']
			user.save()
		elif request.POST.get('name', False) == 'phone_number':
			up.phone_number = request.POST['value']
			up.save()
		elif request.POST.get('name', False) == 'start_date':
			up.start_date = request.POST['value']
			up.save()
		elif request.POST.get('name', False) == 'end_date':
			up.end_date = request.POST['value']
			up.save
		elif request.POST.get('name', False) == 'annual_pay':
			up.annual_pay = request.POST['value']
			up.save()
		elif 'picture' in request.FILES:
			profile_pic_form = ProfilePicChangeForm(request.POST, request.FILES)
			if profile_pic_form.is_valid():
				up.picture = request.FILES['picture']
				up.save()

	return render_to_response('website/me.html', context_instance=RequestContext(request, {'up':up, 'profile_pic': profile_pic_form}))












