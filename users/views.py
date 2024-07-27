from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form, 'title': 'Register'})

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {'title' : 'Logged out'})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title' : 'Profile'})


#messages.debug 
#messages.info
#messages.success
#messages.warning
#messages.error

