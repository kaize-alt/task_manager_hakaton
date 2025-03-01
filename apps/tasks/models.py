from django.db import models
from apps.users.models import CustomUser


class Board(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Board"


class Task(models.Model):
    STATUS_CHOICES = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
    ]
    PRIORITY_CHOICES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="To Do",
    )
    priority = models.IntegerField(PRIORITY_CHOICES, default=2)
    deadline = models.DateTimeField(null=True, blank=True)

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_tasks")
    assigned_to = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"


class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}..."

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
