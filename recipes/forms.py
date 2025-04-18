from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','image', 'ingredients', 'cooking_steps', 'date_created','prep_time','cook_time']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')