from django.contrib import admin
from .models import Board, Task, Comment

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'deadline', 'author', 'assigned_to', 'created_at', 'updated_at')
    search_fields = ('title', 'status', 'priority', 'author__username', 'assigned_to__username')
    ordering = ('-priority', '-deadline', '-created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'text', 'created_at')
    search_fields = ('task__title', 'user__username', 'text')
    ordering = ('-created_at',)
