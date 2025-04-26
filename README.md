# Food Recipes
Welcome to Food Recipes, a web application build with Django for managing your faviorite recipes and ability to inspire from othere recipes created by different users

## Features
- **User Authentication**: Secure user registration and login.
- **Recipe CRUD**: Create, Read, Update, and Delete recipes created by you.
- **Add immages**: Add an tasty immage along with your recipe if you want
- **Search**: Quickly find recipes by title
- **Order By**: Order recipes ascending by title and date 
- **User Profiles**: Edit your profile
- **View all recipes**: You can view all the recipes available from all the users even if you are not registered or logged in
- **Pagination**: for a better navigation a pagination is available at your disposall
- **View recipes by users**: You can view all recipes created by a specific user just by clicking the user that created a certain recipe
- **Main page show recipes**: main page will show the name of the recipe, total cook time, user and date created.
- **Detail view of a recipe**: by cliking a recipe you will be able to see a detail view of a recipe, to edit or delete the recipe if you are the creator.

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
  

