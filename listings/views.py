from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

def browse(request):
    return render(request, 'website/browse.html', {'request':request})

def post(request):
    context = RequestContext(request)
    return render_to_response(
            'website/post.html',
            {'request':request}, context)
