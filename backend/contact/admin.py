from django.contrib import admin
from .models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "email",
    )

    list_editable = (
        "is_active",
    )

    fieldsets = (
        (
            "Contact Information",
            {
                "fields": (
                    "name",
                    "email",
                    "github_url",
                    "linkedin_url",
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