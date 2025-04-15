import pytest
from django.contrib.auth import get_user_model
from recipes.models import Recipe


@pytest.mark.django_db
def test_create_recipe():
    user = get_user_model().objects.create_user(username="user1", password="testing321")
    recipe = Recipe.objects.create(title="Carbonara",
                                  ingredients="paste,sos",
                                  cooking_steps="sdfs",
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
