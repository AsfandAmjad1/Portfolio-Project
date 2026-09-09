from django.shortcuts import render
from .models import SkillCategory


def skills(request):
    categories = SkillCategory.objects.filter(
        is_active=True
    ).prefetch_related("skills")

    return render(
        request,
        "skills/skills.html",
        {"categories": categories}
    )