from django.db import models


class Experience(models.Model):

    EXPERIENCE_TYPES = [
        ("internship", "Internship"),
        ("job", "Job"),
    ]

    title = models.CharField(max_length=150)
    company = models.CharField(max_length=200)

    experience_type = models.CharField(
        max_length=20,
        choices=EXPERIENCE_TYPES,
        default="internship",
    )

    location = models.CharField(
        max_length=150,
        blank=True,
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True,
    )

    is_current = models.BooleanField(
        default=False,
        help_text="Select this if you are currently working here.",
    )

    description = models.TextField()

    technologies = models.CharField(
        max_length=500,
        blank=True,
        help_text="Enter technologies separated by commas."
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["display_order", "-start_date"]
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.title} - {self.company}"