from django.shortcuts import render

from .models import (
    AboutProfile,
    PersonalInformation,
    CareerObjective,
    CareerInterest,
)


def about(request):
    profile = AboutProfile.objects.filter(
        is_active=True
    ).first()

    personal_information = PersonalInformation.objects.filter(
        is_active=True
    ).order_by(
        "display_order",
        "id",
    )

    career_objective = CareerObjective.objects.filter(
        is_active=True
    ).first()

    career_interests = CareerInterest.objects.filter(
        is_active=True
    ).order_by(
        "display_order",
        "id",
    )

    context = {
        "profile": profile,
        "personal_information": personal_information,
        "career_objective": career_objective,
        "career_interests": career_interests,
    }

    return render(
        request,
        "about/about.html",
        context,
    )