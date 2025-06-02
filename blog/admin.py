from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "watched_count",
        "is_published",
        "created_at",
        "updated_at",
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
