from django.contrib import admin
from django.utils.html import format_html

from yboga.admin.game.game_component import GameComponentInline
from yboga.admin.game.game_explansion import GameExpansionInline
from yboga.admin.game.game_feature import GameFeatureInline
from yboga.admin.game.game_image import GameImageInline
from yboga.models.game.game import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "release_date", "cover_preview")
    list_filter = ("categories", "release_date", "publisher")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        GameImageInline,
        GameFeatureInline,
        GameComponentInline,
        GameExpansionInline,
    ]

    def cover_preview(self, obj):
        if obj.image:
            return format_html(f"<img src='{obj.image.url}' height='50' />")
        return "-"

    cover_preview.short_description = "Обложка"
