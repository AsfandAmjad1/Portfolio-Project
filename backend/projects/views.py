from django.shortcuts import render
from .models import Project


def projects(request):
    professional_projects = Project.objects.filter(
        category="professional",
        is_active=True
    ).order_by("display_order", "-created_at")[:3]

    academic_projects = Project.objects.filter(
        category="academic",
        is_active=True
    ).order_by("display_order", "-created_at")[:3]

    personal_projects = Project.objects.filter(
        category="personal",
        is_active=True
    ).order_by("display_order", "-created_at")[:3]

    context = {
        "professional_projects": professional_projects,
        "academic_projects": academic_projects,
        "personal_projects": personal_projects,
    }

    return render(request, "projects/projects.html", context)


def project_category(request, category):

    valid_categories = [
        "professional",
        "academic",
        "personal",
    ]

    if category not in valid_categories:
        return render(
            request,
            "projects/projects.html",
            status=404
        )

    project_list = Project.objects.filter(
        category=category,
        is_active=True
    ).order_by("display_order", "-created_at")

    category_names = {
        "professional": "Professional Projects",
        "academic": "Academic Projects",
        "personal": "Personal Projects",
    }

    context = {
        "projects": project_list,
        "category": category,
        "category_name": category_names[category],
    }

    return render(request, "projects/category.html", context)