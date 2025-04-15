from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import UserRegisterForm, UserUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #the below message will be a flashed message, one time-alert
            messages.success(request, f'Your account has been created. You are now able to Log In')
            return redirect('login')
    else:
        form = UserRegisterForm() #created a user using the form provided by django
    return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipes-home')
        else:
            messages.error(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})

@csrf_exempt
def logout_view(request):
      if request.method == 'POST':
        logout(request)
        return render(request, 'accounts/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
         u_form = UserUpdateForm(request.POST, instance=request.user)
         if u_form.is_valid():
             u_form.save()
             messages.info(request,f'Your Account has been updated!')
         else:
             messages.warning(request, f'The account already exists!')
         return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html',{'u_form':u_form})
