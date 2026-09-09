from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_featured",
        "display_order",
        "is_active",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "technologies",
    )

    list_editable = (
        "display_order",
        "is_featured",
        "is_active",
    )

    ordering = (
        "category",
        "display_order",
        "-created_at",
    )

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "category",
                    "short_description",
                    "technologies",
                    "image",
                )
            },
        ),
        (
            "Project Links",
            {
                "fields": (
                    "github_url",
                    "live_url",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_featured",
                    "is_active",
                )
            },
        ),
    )