from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    recipes = Recipe.objects.all()

    for recipe in recipes:
        total_time = format_total_cook_time(recipe.prep_time + recipe.cook_time)
        recipe.total_time = total_time  # Attach to each recipe instance

    context = {
        'recipes': recipes
    }

    return render(request, 'recipes/home.html',context)

# create function that will format the Total cooking time
def format_total_cook_time(duration):
    hours = duration // 60
    minutes = duration % 60
    minute_descriptor  = "minute" if minutes == 1 else "minutes"
    hour_descriptor  = "hour" if hours == 1 else "hours"

    return "{hours} {hour_descriptor} {minutes} {minute_descriptor}".format(hours=hours, minutes=minutes,
                                                                            minute_descriptor=minute_descriptor,
                                                                            hour_descriptor=hour_descriptor)

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
