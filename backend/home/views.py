from django.shortcuts import render
from .models import HomeProfile


def home(request):
    profile = HomeProfile.objects.filter(is_active=True).first()

    context = {
        "profile": profile,
    }

    return render(request, "home/home.html", context)