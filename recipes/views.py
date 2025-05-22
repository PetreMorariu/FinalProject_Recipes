from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm, SearchForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .functions import pagination,format_total_cook_time


def home(request):
    recipes = Recipe.objects.all().order_by('-date_created')
    context = pagination(request, recipes)
    return render(request, 'recipes/home.html', context)

def detail_view_recipe_v2(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.all()

    context = {
        'recipe': recipe,
        'comments': comments,
    }
    return render(request, 'recipes/detail_recipe_v2.html', context)


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES) #request.FILES will make sure to get the image as well
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, f'Your recipe has been created!')
            return redirect('recipes-home')
        else:
            messages.error(request, f"Please correct the errors")
            return render(request, 'recipes/add_recipe.html', {'form': form})
    else:
        form = RecipeForm()
        return render(request, 'recipes/add_recipe.html', {'form':form})

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            return redirect('detail-recipes', recipe_id=recipe.id)
    return render(request, 'recipes/comment_recipe.html',{'form':form,'recipe':recipe})




@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)  # Populate form with the existing recipe
        if form.is_valid():
            form.save()  # Update the recipe instance in the database
            messages.success(request, f'Your recipe has been updated!')
            return redirect('detail-recipes', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)  # Pre-fill the form with recipe data

    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == 'POST':
        recipe.delete()
        messages.warning(request, f'Your recipe was deleted!')
        return redirect("recipes-home")
    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})


def sort_recipe_by_title(request):
    recipes = Recipe.objects.all().order_by('title')
    context = pagination(request, recipes)
    return render(request, 'recipes/sort_title.html', context)


def sort_recipe_by_date(request):
    recipes = Recipe.objects.all().order_by('date_created')
    context = pagination(request, recipes)
    return render(request, 'recipes/sort_date_created.html', context)

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

def search(request):
    form = SearchForm()
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Recipe.objects.filter(title__icontains=query)  # Search in the title

    for recipe in results:
        total_time = format_total_cook_time(recipe.prep_time + recipe.cook_time)
        recipe.total_time = total_time  # Attach to each recipe instance

    return render(request, 'recipes/search.html', {'form': form, 'results': results})









