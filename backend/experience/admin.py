from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "experience_type",
        "start_date",
        "end_date",
        "is_current",
        "display_order",
        "is_active",
    )

    list_filter = (
        "experience_type",
        "is_current",
        "is_active",
    )

    search_fields = (
        "title",
        "company",
        "description",
        "technologies",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "-start_date",
    )

    fieldsets = (
        (
            "Experience Details",
            {
                "fields": (
                    "title",
                    "company",
                    "experience_type",
                    "location",
                )
            },
        ),
        (
            "Duration",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "is_current",
                )
            },
        ),
        (
            "Professional Information",
            {
                "fields": (
                    "description",
                    "technologies",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            },
        ),
    )