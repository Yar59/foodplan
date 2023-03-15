from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
    )
    raw_id_fields = ('not_used_ingr',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    raw_id_fields = ('ingredients', 'likes', 'dislikes')


admin.site.register(Ingredients)
