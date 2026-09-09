from django.contrib import admin

from .models import (
    HomeProfile,
    HomeStats,
    HomeSection,
    HomeService,
    HomeProcess,
    HomeCTA,
)


# =========================================================
# HOME PROFILE
# =========================================================

@admin.register(HomeProfile)
class HomeProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "professional_title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "professional_title",
        "introduction",
    )

    fieldsets = (

        (
            "Profile Information",
            {
                "fields": (
                    "greeting",
                    "name",
                    "professional_title",
                    "introduction",
                )
            },
        ),

        (
            "Profile Media",
            {
                "fields": (
                    "profile_image",
                    "resume",
                )
            },
        ),

        (
            "Hero Buttons",
            {
                "fields": (
                    "work_button_text",
                    "work_button_url",
                    "cv_button_text",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )


# =========================================================
# HOME STATISTICS
# =========================================================

@admin.register(HomeStats)
class HomeStatsAdmin(admin.ModelAdmin):

    list_display = (
        "projects_count",
        "experience_years",
        "technologies_count",
        "achievements_count",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    fieldsets = (

        (
            "Homepage Statistics",
            {
                "fields": (
                    "projects_count",
                    "experience_years",
                    "technologies_count",
                    "achievements_count",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )


# =========================================================
# HOME SECTIONS
# =========================================================

@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):

    list_display = (
        "section_key",
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "section_key",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "label",
    )

    list_editable = (
        "is_active",
    )

    ordering = (
        "section_key",
    )

    fieldsets = (

        (
            "Section Content",
            {
                "fields": (
                    "section_key",
                    "label",
                    "title",
                    "description",
                )
            },
        ),

        (
            "Display",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )


# =========================================================
# HOME SERVICES
# =========================================================

@admin.register(HomeService)
class HomeServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "short_code",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "short_code",
        "description",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "-created_at",
    )

    fieldsets = (

        (
            "Service Information",
            {
                "fields": (
                    "title",
                    "short_code",
                    "description",
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


# =========================================================
# HOME PROCESS
# =========================================================

@admin.register(HomeProcess)
class HomeProcessAdmin(admin.ModelAdmin):

    list_display = (
        "step_number",
        "title",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "display_order",
        "step_number",
    )

    fieldsets = (

        (
            "Process Step",
            {
                "fields": (
                    "step_number",
                    "title",
                    "description",
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


# =========================================================
# HOME CTA
# =========================================================

@admin.register(HomeCTA)
class HomeCTAAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "button_text",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "button_text",
    )

    fieldsets = (

        (
            "CTA Content",
            {
                "fields": (
                    "label",
                    "title",
                    "description",
                )
            },
        ),

        (
            "CTA Button",
            {
                "fields": (
                    "button_text",
                    "button_url",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )