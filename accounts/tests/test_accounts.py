import pytest
from django.test import client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


@pytest.fixture
def user(db):
    return User.objects.create_user(username="petre",password="testing321")

@pytest.fixture
def client_logged_in(client: client.Client, user):
    client.login(username="petre", password="testing321")
    return client

@pytest.mark.django_db
def test_create_user():
    user = get_user_model().objects.create_user(username="user1", password="testing321",email="user1@company.com")
    assert user is not None
    assert user.username == "user1"
    assert user.email == "user1@company.com"
    assert len(get_user_model().objects.all()) == 1

def test_create_profile():
    profile = get_user_model().profile
    assert profile is not None

def test_login_view(client_logged_in,user):
    url = '/login/'
    response = client_logged_in.get(url)
    decode = response.content.decode()

    assert response.status_code == 200
    assert "Username" in decode

def test_view_profile(client_logged_in,user):
    url = '/profile/'
    response = client_logged_in.get(url)
    decoded = response.content.decode()

    assert response.status_code == 200
    assert "Profile Info" in decoded

def test_edit_profile(client_logged_in,user):
    url = '/profile/edit/'
    response = client_logged_in.get(url)
    decoded = response.content.decode()

    assert response.status_code == 200
    assert "Profile Edit" in decoded