# Food Recipes
Welcome to Food Recipes, a web application build with Django for managing your faviorite recipes and ability to inspire from othere recipes created by different users

## Features
- **User Authentication**: Secure user registration and login. Once a new user is created, a User Profile will be automatically created for that user.
- **Recipe CRUD**: Create, Read, Update, and Delete recipes created by you.
- **Add immages**: Add an tasty immage along with your recipe if you want
- **Search**: Quickly find recipes by title
- **Order By**: Order recipes ascending by title and date 
- **User Profiles**: Edit your profile
- **View all recipes**: You can view all the recipes available from all the users even if you are not registered or logged in
- **View recipes by users**: You can view all recipes created by a specific user just by clicking the user that created a certain recipe
- **Pagination**: for a better navigation a pagination is available at your disposall
- **Main page show recipes**: main page will show the name of the recipe, total cook time, user and date created.
- **Detail view of a recipe**: by cliking a recipe you will be able to see a detail view of a recipe and to edit or delete the recipe if you are the creator.

## Technologies used

- Python 3.x
- Django 4.x
- SQLite
- HTML5 & CSS
- Bootstrap 4
- Crispy forms

## Installation

### Prerequisites

Make sure you have Python and pip installed on your machine.

### Follow the below steps

- **Get the application from the Github repo**: https://github.com/PetreMorariu/FinalProject_Recipes
- **Copy the app on a path to yout computer**: (eg: C:\django_recipes)
- **Go to that path**: cd C:\django_recipes from a CMD run as Administrator
- **Create the virtual env**:  python -m venv venv
- **Activate the venv**: venv\Scripts\activate, After activation, your command prompt should change to indicate that you are now working inside the virtual environment.
- **Install Project Dependencies**: pip install -r packages.txt
- **Run database migrations**:python manage.py migrate
- **Start the Django development server**:python manage.py runserver

### Populate the database with a few demo recipes
  If you want to have an initial set of recipes please follow the  steps from add_recipes.txt using recipes.json available in the project

## URL's available for the application
###
- **''** is the Recipes Home Page showing all the recipes paginated
- **'recipes/<int:recipe_id>/'** will show a detail view for a specific recipe
- **'recipes/add/'** will add a new recipe for the logged in user
- **'recipes/<int:recipe_id>/edit/** will edit a recipe
- **'recipes/<int:recipe_id>/delete/'** will delete a recipe
- **'recipes/sort_title/'** will sort the recipes by title ascending
- **'recipes/sort_date/'** will sort the recipes by date ascending
- **'recipes/user/'** will show all te recipes for a certain user (it does not need to be the logged in user)
- **'recipes/search/'** will open a page for a search based on the title
###
- **'login/'** user login page
- **'logout/'** user logout page
- **'register/'** user registration page
- **'profile/'** user profile page
- **'profile/edit/'** user edit profile page

  

