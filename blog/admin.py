from django.contrib import admin

from .admin_models.post_admin import PostAdmin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
