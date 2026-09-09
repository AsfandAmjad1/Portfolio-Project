from django.shortcuts import render
from .models import Experience


def experience(request):
    experiences = Experience.objects.filter(
        is_active=True
    )

    return render(
        request,
        "experience/experience.html",
        {"experiences": experiences}
    )