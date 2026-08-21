from django.contrib import admin
from .models import HomeProfile


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

    readonly_fields = (
        "created_at",
        "updated_at",
    )