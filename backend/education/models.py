from django.db import models


class Education(models.Model):
    DEGREE_CHOICES = [
        ("matric", "Matric"),
        ("intermediate", "Intermediate"),
        ("bachelor", "Bachelor's"),
        ("master", "Master's"),
        ("other", "Other"),
    ]

    degree = models.CharField(
        max_length=150
    )

    degree_type = models.CharField(
        max_length=20,
        choices=DEGREE_CHOICES,
        default="other",
    )

    institute = models.CharField(
        max_length=200
    )

    board = models.CharField(
        max_length=200,
        blank=True,
        help_text="Enter the board for school/college education."
    )

    start_year = models.PositiveIntegerField()

    end_year = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    is_current = models.BooleanField(
        default=False,
        help_text="Select this if you are currently studying here."
    )

    grade = models.CharField(
        max_length=20,
        blank=True,
        help_text="For Matric/Intermediate, e.g. A+ or A."
    )

    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="For university education, e.g. 3.60."
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
        ordering = ["display_order", "-start_year"]
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institute}"