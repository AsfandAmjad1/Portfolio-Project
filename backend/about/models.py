from django.db import models


class AboutProfile(models.Model):
    title = models.CharField(
        max_length=200,
        default="About Me"
    )

    introduction_heading = models.CharField(
        max_length=150,
        default="My Introduction"
    )

    introduction = models.TextField()

    tagline = models.CharField(
        max_length=250,
        default="Turning Complexity into Clarity."
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
        verbose_name = "About Profile"
        verbose_name_plural = "About Profile"

    def __str__(self):
        return self.title


class PersonalInformation(models.Model):
    label = models.CharField(
        max_length=100
    )

    value = models.CharField(
        max_length=250
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
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.label


class CareerObjective(models.Model):
    title = models.CharField(
        max_length=150,
        default="Career Objective"
    )

    objective = models.TextField()

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
        verbose_name = "Career Objective"
        verbose_name_plural = "Career Objective"

    def __str__(self):
        return self.title


class CareerInterest(models.Model):
    title = models.CharField(
        max_length=150
    )

    short_code = models.CharField(
        max_length=10,
        blank=True,
        help_text="Example: AI, DA, SD"
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
        verbose_name = "Career Interest"
        verbose_name_plural = "Career Interests"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title