from django.contrib import admin
from django.utils.html import format_html

from yboga.models.game.game_component import GameComponent


@admin.register(GameComponent)
class GameComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "game", "quantity", "component_preview")
    list_filter = ("game",)
    search_fields = ("name",)

    def component_preview(self, obj):
        if obj.image:
            return format_html(f"<img src='{obj.image.url}' height='40' />")
        return "-"

    component_preview.short_description = "Изображение"


class GameComponentInline(admin.TabularInline):
    model = GameComponent
    extra = 1
