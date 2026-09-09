from django.contrib import admin

from .models import (
    AboutProfile,
    PersonalInformation,
    CareerObjective,
    CareerInterest,
)


@admin.register(AboutProfile)
class AboutProfileAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "introduction_heading",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "introduction",
        "tagline",
    )

    fieldsets = (
        (
            "Page Information",
            {
                "fields": (
                    "title",
                    "introduction_heading",
                )
            },
        ),
        (
            "Introduction",
            {
                "fields": (
                    "introduction",
                    "tagline",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = (
        "label",
        "value",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "label",
        "value",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "id",
    )


@admin.register(CareerObjective)
class CareerObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "objective",
    )

    fieldsets = (
        (
            "Career Objective",
            {
                "fields": (
                    "title",
                    "objective",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )


@admin.register(CareerInterest)
class CareerInterestAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_code",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "id",
    )