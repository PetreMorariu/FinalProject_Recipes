import pytest
from django.test import client
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture
def user(db):
    return User.objects.create_user(username="petre",password="testing321")

@pytest.fixture
def client_logged_in(client: client.Client, user):
    client.login(username="petre", password="testing321")
    return client

@pytest.fixture
def recipe(user):
    return Recipe.objects.create(title="Carbonara",
                                  ingredients="paste,sos",
                                  cooking_steps="sdfs",
                                  cook_time=34,
                                  prep_time=45,
                                  author=user,
                                  image = "default.jpg")
@pytest.fixture
def recipes(user):
    list_recipes = []
    list_recipes.append(Recipe.objects.create(title="milaneze",
                                  ingredients="paste,sos11",
                                  cooking_steps="steps to cook",
                                  cook_time=70,
                                  prep_time=35,
                                  author=user,
                                  image = "default.jpg"))
    list_recipes.append(Recipe.objects.create(title="Chicken Curry",
                                              ingredients="the ingredients here",
                                              cooking_steps="steps for coocking",
                                              cook_time=25,
                                              prep_time=45,
                                              author=user,
                                              image="default.jpg"))
    return list_recipes



def test_home(client_logged_in, user, recipe):
    response = client_logged_in.get("")
    assert response.status_code == 200
    assert response.content
    assert "Carbonara" in response.content.decode()
    assert user.username in response.content.decode()
    assert user is not None

    #testing "get" for one recipe

    client_logged_in.get("/1/")
    decoded = response.content.decode()
    assert response.status_code == 200
    assert recipe.title in decoded

def test_format_total_cook_time(client_logged_in, user, recipe):
    recipe = recipe
    assert recipe.prep_time == 45
    assert recipe.cook_time == 34

def test_detail_view(client_logged_in,user,recipes):
    url = "/recipes/1/"
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "INGREDIENTS:" in decoded

    url = "/recipes/2/"
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "INGREDIENTS:" in decoded


def test_add_recipe(client_logged_in, user, recipe, recipes):
    url= "/recipes/add/"
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "New Recipe" in decoded

    #creating a dummy image file
    image_file = SimpleUploadedFile(name='default.jpg',content=b'filecontent')

    #test recipe creation
    recipe_dict={ "title":"Chicken Curry",
                  "ingredients":"the ingredients here",
                  "cooking_steps":"steps for coocking",
                  "cook_time":"25",
                  "prep_time":"45",
                  "author":"petre",
                  "image":image_file}
    response = client_logged_in.post(url,recipe_dict)
    assert response.status_code == 200
    assert "New Recipe" in response.content.decode()

def test_edit_recipe(client_logged_in, user, recipe):
    url = "/recipes/1/edit/"
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "Prep time* and Cook time* are displayed in minutes" in decoded


def test_confirm_delete(client_logged_in,user,recipe):
    url = "/recipes/1/delete/"
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "Delete Recipe" in decoded

    assert len(Recipe.objects.all()) == 1

    response = client_logged_in.post("/recipes/1/delete/")
    assert response.status_code == 302
    assert len(Recipe.objects.all()) == 0

def test_sort_recipes_by_title(client_logged_in,user,recipes):
    url = "/recipes/sort_title/"
    response = client_logged_in.get(url)
    decode = response.content.decode()
    assert  response.status_code == 200
    assert "milaneze" in decode


def test_sort_recipes_by_date(client_logged_in,user,recipes):
    url = "/recipes/sort_date/"
    response = client_logged_in.get(url)
    decode = response.content.decode()
    assert  response.status_code == 200
    assert "milaneze" in decode

def test_view_recipes_user(client_logged_in,user,recipes):
    url = "/recipes/user/"
    response = client_logged_in.get(url)
    decode = response.content.decode()
    assert  response.status_code == 200
    assert "Total Cook Time" in decode
