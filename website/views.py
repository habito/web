from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'website/index.html', {})

def browse(request):
    return render(request, 'website/browse.html', {})

#def log_in(request):
 #   username = request.POST['username']
  #  password = request.POST['password']
   # user = authenticate(username=username, password=password)
    #if user is not None:
     #   if user.is_active:
      #      login(request, user)
       #     # Redirect to a success page.
        #else:
            # Return a 'disabled account' error message
    #else:
        # Return an 'invalid login' error message.
