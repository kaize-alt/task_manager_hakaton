from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("worker", "Worker"),
    ]
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="worker")

    def __str__(self):
        return self.username

    def get_role_display(self):
        return dict(self.ROLE_CHOICES).get(self.role, "Unknown")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
