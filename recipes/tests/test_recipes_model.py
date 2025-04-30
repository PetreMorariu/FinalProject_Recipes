from datetime import datetime, timezone

import pytest
from django.contrib.auth import get_user_model
from recipes.models import Recipe,Comment


@pytest.mark.django_db
def test_create_recipe():
    user = get_user_model().objects.create_user(username="user1", password="testing321")
    recipe = Recipe.objects.create(title="Carbonara",
                                  ingredients="paste,sos",
                                  cooking_steps="sdfs",
                                  date_created='2023-10-09 18:00:00',
                                  cook_time=34,
                                  prep_time=45,
                                  author=user,
                                  image = "default.jpg")

    assert recipe.title == "Carbonara"
    assert recipe.ingredients == "paste,sos"
    assert recipe.cooking_steps == "sdfs"
    assert recipe.cook_time == 34
    assert recipe.prep_time == 45
    assert recipe.author == user
    assert recipe.image == "default.jpg"


@pytest.mark.django_db
def test_create_comment():
    user = get_user_model().objects.create_user(username="user1", password="testing321")
    recipe = Recipe.objects.create(title="Carbonara",
                                   ingredients="paste,sos",
                                   cooking_steps="sdfs",
                                   date_created='2023-10-09 18:00:00',
                                   cook_time=34,
                                   prep_time=45,
                                   author=user,
                                   image="default.jpg")

    comment = Comment.objects.create(recipe=recipe,
                                     user=user,
                                     text="Delicious recipe. Do it!",
                                     )
    assert comment.text == "Delicious recipe. Do it!"
    assert comment.recipe.title == "Carbonara"
    assert comment.user.username == "user1"
