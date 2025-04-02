from django.shortcuts import render

recipes = [
    {
       'author': 'PetreM',
       'title': 'Recipe post 1',
       'content' : 'First recipe content',
       'date_posted': 'April 2, 2025',
       'cook_time': '2 hours'

    },
    {
       'author': 'Jane Doe',
       'title': 'Recipe post 2',
       'content' : 'Second recipe content',
       'date_posted': 'April 1, 2025',
       'cook_time': '1 hour'
    },
    {
       'author': 'PetreM',
       'title': 'Recipe post 3',
       'content' : 'Third recipe content',
       'date_posted': 'April 3, 2025',
       'cook_time': '3 hours'
    }
]

def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/home.html',context)

def about(request):
    return  render(request, 'recipes/about.html', {'title':'About'})