from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from user_profile.forms import *


def index(request):
	
    return render(request, 'website/index.html', {'request':request})

