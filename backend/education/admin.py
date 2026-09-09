from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "institute",
        "degree_type",
        "start_year",
        "end_year",
        "is_current",
        "display_order",
        "is_active",
    )

    list_filter = (
        "degree_type",
        "is_current",
        "is_active",
    )

    search_fields = (
        "degree",
        "institute",
        "board",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "-start_year",
    )

    fieldsets = (
        (
            "Education Details",
            {
                "fields": (
                    "degree",
                    "degree_type",
                    "institute",
                    "board",
                )
            },
        ),
        (
            "Academic Period",
            {
                "fields": (
                    "start_year",
                    "end_year",
                    "is_current",
                )
            },
        ),
        (
            "Academic Result",
            {
                "fields": (
                    "grade",
                    "cgpa",
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