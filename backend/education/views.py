from django.shortcuts import render
from .models import Education


def education(request):
    educations = Education.objects.filter(
        is_active=True
    )

    return render(
        request,
        "education/education.html",
        {"educations": educations}
    )