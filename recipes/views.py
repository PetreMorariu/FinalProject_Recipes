from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/home.html',context)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, f'Your recipe has been created!')
            return redirect('recipes-home')
    else:
        form = RecipeForm()
        return render(request, 'recipes/add_recipe.html', {'form':form})

def about(request):
    return  render(request, 'recipes/about.html', {'title':'About'})
