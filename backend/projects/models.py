from django.db import models


class Project(models.Model):

    CATEGORY_CHOICES = [
        ("professional", "Professional Projects"),
        ("academic", "Academic Projects"),
        ("personal", "Personal Projects"),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="personal",
    )

    short_description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        help_text="Example: Django, Python, PostgreSQL"
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    github_url = models.URLField(blank=True)

    live_url = models.URLField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    is_featured = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title