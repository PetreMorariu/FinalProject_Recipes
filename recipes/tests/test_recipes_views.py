import pytest
from django.test import client
from django.contrib.auth.models import User
from recipes.models import Recipe

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

def test_home(client_logged_in, user, recipe):
    response = client_logged_in.get("")
    assert response.status_code == 200
    assert response.content
    assert "Carbonara" in response.content.decode()
    assert user.username in response.content.decode()
    assert user is not None

