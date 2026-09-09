from django.shortcuts import render
from django.utils import timezone

from .models import (
    HomeProfile,
    HomeStats,
    HomeSection,
    HomeService,
    HomeProcess,
    HomeCTA,
)

from projects.models import Project
from skills.models import Skill
from experience.models import Experience


def home(request):
    profile = HomeProfile.objects.filter(is_active=True).first()
    stats = HomeStats.objects.filter(is_active=True).first()

    projects_count = Project.objects.filter(
        is_active=True
    ).count()

    technologies_count = Skill.objects.filter(
        is_active=True
    ).count()

    experiences = Experience.objects.filter(
        is_active=True
    )

    total_days = 0
    today = timezone.now().date()

    for experience in experiences:
        end_date = today if experience.is_current else experience.end_date

        if end_date:
            total_days += (
                end_date - experience.start_date
            ).days

    experience_years = round(
        total_days / 365.25,
        1
    )

    sections = {
        section.section_key: section
        for section in HomeSection.objects.filter(
            is_active=True
        )
    }

    services = HomeService.objects.filter(
        is_active=True
    ).order_by(
        "display_order",
        "-created_at"
    )

    featured_projects = Project.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by(
        "display_order",
        "-created_at"
    )[:3]

    process_steps = HomeProcess.objects.filter(
        is_active=True
    ).order_by(
        "display_order",
        "step_number"
    )

    cta = HomeCTA.objects.filter(
        is_active=True
    ).first()

    context = {
        "profile": profile,
        "stats": stats,
        "sections": sections,
        "services": services,
        "featured_projects": featured_projects,
        "process_steps": process_steps,
        "cta": cta,
        "projects_count": projects_count,
        "technologies_count": technologies_count,
        "experience_years": experience_years,
    }

    return render(
        request,
        "home/home.html",
        context
    )