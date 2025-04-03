from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #the below message will be a flashed message, one time-alert
            messages.success(request, f'Account for {username} has been created!')
            return redirect('recipes-home')
    else:
        form = UserRegisterForm() #created a user using the form provided by django
    return render(request, 'accounts/register.html', {'form':form})
