from django.contrib import admin

from yboga.models.game.game_explansion import GameExpansion


@admin.register(GameExpansion)
class GameExpansionAdmin(admin.ModelAdmin):
    list_display = ("title", "game", "release_date")
    list_filter = ("game", "release_date")
    search_fields = ("title", "description")


class GameExpansionInline(admin.TabularInline):
    model = GameExpansion
    extra = 0
