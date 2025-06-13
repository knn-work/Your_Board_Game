from django.contrib import admin
from django.utils.html import format_html

from yboga.models.game.game_image import GameImage


@admin.register(GameImage)
class GameImageAdmin(admin.ModelAdmin):
    list_display = ("game", "caption", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html(f"<img src='{obj.image.url}' height='100' />")
        return "-"

    preview.short_description = "Превью"


class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 1
