from django.shortcuts import render
from .models import Achievement


def achievements(request):
    achievements_list = Achievement.objects.filter(
        is_active=True
    ).order_by("display_order", "-date")

    context = {
        "achievements": achievements_list,
    }

    return render(request, "achievements/achievements.html", context)