import os

from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    cooking_steps = models.TextField()
    date_created = models.DateTimeField(default=timezone.now())
    cook_time = models.IntegerField()
    prep_time = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #create a one-many connection;If User will be deleted, then his recipes will be deleted as well
    #add an immage for a recipe
    image = models.ImageField(default='default.jpg', upload_to='recipe_images')

    def __str__(self):
        return self.title

    #This delete override will make sure to remove the image for the recipe stored as well
    # at recipe delete time
    def delete(self, *args, **kwargs):
        image_path = self.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        super().delete(*args, **kwargs)

    # def save(self, *args, **kwarg):
    #     super().save(*args, **kwarg)
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    data_created_comment = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.text}'
