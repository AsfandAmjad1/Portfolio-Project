from django.contrib import admin
from .models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organization",
        "date",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
        "organization",
    )

    search_fields = (
        "title",
        "organization",
        "description",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "-date",
    )