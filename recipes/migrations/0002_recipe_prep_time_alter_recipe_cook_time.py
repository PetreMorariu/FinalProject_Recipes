# Generated by Django 5.1.7 on 2025-04-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(),
        ),
    ]
