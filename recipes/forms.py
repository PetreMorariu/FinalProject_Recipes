from django import forms
from .models import Recipe,Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','image', 'ingredients', 'cooking_steps', 'date_created','prep_time','cook_time']

        labels = {
            'prep_time': 'Preparation Time (mins)',
            'cook_time': 'Cooking Time (mins)',
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']