from django.core.paginator import Paginator

#create pagination function
def pagination(request, recipes):
    paginator = Paginator(recipes, 7)
    page_number = request.GET.get('page')
    recipe_page = paginator.get_page(page_number)

    # Attach total_time to each recipe in the paginated page
    for recipe in recipe_page:
        total_time = format_total_cook_time(recipe.prep_time + recipe.cook_time)
        recipe.total_time = total_time

    return {
        'recipes': recipe_page,
    }

# create function that will format the Total cooking time
def format_total_cook_time(duration):
    hours = duration // 60
    minutes = duration % 60
    minute_descriptor  = "minute" if minutes == 1 else "minutes"
    hour_descriptor  = "hour" if hours == 1 else "hours"

    return "{hours} {hour_descriptor} {minutes} {minute_descriptor}".format(hours=hours, minutes=minutes,
                                                                            minute_descriptor=minute_descriptor,
                                                                            hour_descriptor=hour_descriptor)
