from django.contrib import admin
from .models import Post, Category

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_categories')
    filter_horizontal = ('categories',)

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'


