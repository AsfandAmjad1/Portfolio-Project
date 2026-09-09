from django.contrib import admin
from .models import SkillCategory, Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("name", "logo", "display_order", "is_active")


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_order", "is_active")
    list_editable = ("display_order", "is_active")
    search_fields = ("name",)
    ordering = ("display_order", "name")
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "display_order", "is_active")
    list_filter = ("category", "is_active")
    list_editable = ("display_order", "is_active")
    search_fields = ("name",)
    ordering = ("category", "display_order", "name")