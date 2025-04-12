from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home(request):
    recipes = Recipe.objects.all()

    for recipe in recipes:
        total_time = format_total_cook_time(recipe.prep_time + recipe.cook_time)
        recipe.total_time = total_time  # Attach to each recipe instance

    paginator = Paginator(recipes,5)
    page_number = request.GET.get('page')  # Get the page number from GET request
    page_obj = paginator.get_page(page_number)

    context = {
        'recipes': page_obj
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

def detail_view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    form = RecipeForm(instance=recipe)

    # Disable all the fields in the form
    for field in form:
        field.field.widget.attrs['disabled'] = 'disabled'# the form fields are disabled(read-only)

    return render(request, 'recipes/detail_recipe.html', {'form': form, 'object': recipe})


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



@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)  # Populate form with the existing recipe
        if form.is_valid():
            form.save()  # Update the recipe instance in the database
            messages.success(request, f'Your recipe has been updated!')
            return redirect('recipes-home')
    else:
        form = RecipeForm(instance=recipe)  # Pre-fill the form with recipe data

    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect("recipes-home")
    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})



def sort_recipe_by_title(request):
    recipes = Recipe.objects.all()
    recipes_list = []
    for recipe in recipes:
        recipes_list.append(recipe)
    recipes_list.sort(key=lambda recipe: recipe.title)
    return render(request, 'recipes/sort_title.html', {'recipes': recipes_list})



def view_recipes_user(request):
    author = request.GET.get('author')
    if author:
        recipes = Recipe.objects.filter(author__username=author)
    else:
        recipes = Recipe.objects.all()

    for recipe in recipes:
        total_time = format_total_cook_time(recipe.prep_time + recipe.cook_time)
        recipe.total_time = total_time  # Attach to each recipe instance
    context = {
        'recipes': recipes
    }

    return render(request, 'recipes/one_user_recipes.html', context)






