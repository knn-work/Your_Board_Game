from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "watched_count",
        "category",
        "is_published",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    readonly_fields = ("watched_count",)
    list_filter = (
        "id",
        "title",
        "category",
        "is_published",
        "created_at",
        "updated_at",
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
