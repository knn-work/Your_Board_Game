from django.contrib import admin

from yboga.models.game.game_feature import GameFeature


@admin.register(GameFeature)
class GameFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "game")
    search_fields = ("title", "description")
    list_filter = ("game",)


class GameFeatureInline(admin.TabularInline):
    model = GameFeature
    extra = 1
