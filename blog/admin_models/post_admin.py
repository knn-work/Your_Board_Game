from django.contrib import admin
from django.utils.safestring import mark_safe

from conf.settings import BASE_DIR


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "get_photo",
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

    def get_photo(self, obj):
        if not obj.photo:
            return mark_safe(
                f"<img src='https://media.istockphoto.com/id/1222357475/vector/image-preview-icon-picture-placeholder-for-website-or-ui-ux-design-vector-illustration.jpg?s=612x612&w=0&k=20&c=KuCo-dRBYV7nz2gbk4J9w1WtTAgpTdznHu55W9FjimE=' width='50' height='50'>"
            )
        path = f"{BASE_DIR}/{obj.photo.url}".replace("\\", "/")
        return mark_safe(
            f"<img src='{obj.photo.url}' width='{50*obj.photo.width//obj.photo.height}' height='50'>"
        )

    get_photo.short_description = "Изображение"
