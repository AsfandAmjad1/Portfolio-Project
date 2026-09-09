from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.projects, name="projects"),
    path("<str:category>/", views.project_category, name="project_category"),
]