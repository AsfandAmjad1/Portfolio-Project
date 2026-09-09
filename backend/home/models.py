from django.db import models


# =========================================================
# HOME PROFILE
# =========================================================

class HomeProfile(models.Model):

    greeting = models.CharField(
        max_length=100,
        default="Hello, I'm"
    )

    name = models.CharField(
        max_length=150
    )

    professional_title = models.CharField(
        max_length=200
    )

    introduction = models.TextField()

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    work_button_text = models.CharField(
        max_length=100,
        default="View My Work"
    )

    work_button_url = models.CharField(
        max_length=300,
        default="/projects/"
    )

    cv_button_text = models.CharField(
        max_length=100,
        default="Download My CV"
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
        verbose_name = "Home Profile"
        verbose_name_plural = "Home Profile"

    def __str__(self):
        return self.name


# =========================================================
# HOME STATISTICS
# =========================================================

class HomeStats(models.Model):

    projects_count = models.PositiveIntegerField(
        default=0
    )

    experience_years = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0
    )

    technologies_count = models.PositiveIntegerField(
        default=0
    )

    achievements_count = models.PositiveIntegerField(
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
        verbose_name = "Home Statistics"
        verbose_name_plural = "Home Statistics"

    def __str__(self):
        return "Homepage Statistics"


# =========================================================
# HOME SECTIONS
# =========================================================

class HomeSection(models.Model):

    SECTION_CHOICES = [
        ("services", "Services"),
        ("projects", "Featured Projects"),
        ("process", "My Process"),
    ]

    section_key = models.CharField(
        max_length=30,
        choices=SECTION_CHOICES,
        unique=True
    )

    label = models.CharField(
        max_length=100,
        blank=True
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
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
        verbose_name = "Home Section"
        verbose_name_plural = "Home Sections"

    def __str__(self):
        return self.get_section_key_display()


# =========================================================
# HOME SERVICES
# =========================================================

class HomeService(models.Model):

    title = models.CharField(
        max_length=150
    )

    short_code = models.CharField(
        max_length=5,
        help_text="Example: AI, DA, SE, WD"
    )

    description = models.TextField()

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
        verbose_name = "Home Service"
        verbose_name_plural = "Home Services"
        ordering = [
            "display_order",
            "-created_at"
        ]

    def __str__(self):
        return self.title


# =========================================================
# HOME PROCESS
# =========================================================

class HomeProcess(models.Model):

    step_number = models.PositiveIntegerField(
        default=1
    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

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
        verbose_name = "Home Process Step"
        verbose_name_plural = "Home Process Steps"
        ordering = [
            "display_order",
            "step_number"
        ]

    def __str__(self):
        return f"{self.step_number:02d} - {self.title}"


# =========================================================
# HOME CTA
# =========================================================

class HomeCTA(models.Model):

    label = models.CharField(
        max_length=100,
        default="Let's Talk"
    )

    title = models.CharField(
        max_length=200,
        default="Let's Work Together"
    )

    description = models.TextField(
        blank=True
    )

    button_text = models.CharField(
        max_length=100,
        default="Get In Touch"
    )

    button_url = models.CharField(
        max_length=300,
        default="/contact/"
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
        verbose_name = "Home CTA"
        verbose_name_plural = "Home CTA"

    def __str__(self):
        return self.title