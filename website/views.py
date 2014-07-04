from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html', {})

def browse(request):
    return render(request, 'website/browse.html', {})
