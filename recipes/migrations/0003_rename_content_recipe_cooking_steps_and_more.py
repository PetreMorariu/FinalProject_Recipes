# Generated by Django 5.1.7 on 2025-04-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_prep_time_alter_recipe_cook_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='content',
            new_name='cooking_steps',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
