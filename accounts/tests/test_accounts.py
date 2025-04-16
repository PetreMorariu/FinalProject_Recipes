import pytest
from django.contrib.auth import get_user_model
from accounts.models import Profile


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