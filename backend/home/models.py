from django.db import models


class HomeProfile(models.Model):
    greeting = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    professional_title = models.CharField(max_length=200)
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

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Profile"
        verbose_name_plural = "Home Profile"

    def __str__(self):
        return self.name
    