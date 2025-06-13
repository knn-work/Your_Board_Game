from django.contrib import admin
from django.utils.html import format_html

from yboga.models.publisher import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "website_link", "logo_preview")
    search_fields = ("name",)

    def website_link(self, obj):
        if obj.website:
            return format_html(
                f"<a href='{obj.website}' target='_blank'>{obj.website}</a>"
            )
        return "-"

    website_link.short_description = "Сайт"

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(f"<img src='{obj.logo.url}' height='40' />")
        return "-"

    logo_preview.short_description = "Логотип"
