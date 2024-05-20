from django.contrib import admin

from .models import Category, Recipe

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    ...


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)

# ou fazer assim
# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#    ...

'''
ou fazer assim
def register_models(*models):
    for model in models:
        admin.site.register(model, admin.ModelAdmin)
    return None


register_models(Category, Recipe)
'''
