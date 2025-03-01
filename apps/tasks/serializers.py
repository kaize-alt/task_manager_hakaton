from rest_framework import serializers
from .models import Board, Table, Task, Comment
from apps.users.models import CustomUser


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("id", "name", "created_at",)


class TableSerializer(serializers.ModelSerializer):
    board_name = serializers.CharField(source="board.name", read_only=True)

    class Meta:
        model = Table
        fields = ("id", "name", "board", "board_name", "created_at",)


class TaskSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    assigned_to_name = serializers.CharField(source="assigned_to.username", read_only=True, default=None)
    table_name = serializers.CharField(source="table.name", read_only=True)

    class Meta:
        model = Task
        fields = (
            "id", "title", "description", "status", "priority", "deadline",
            "author", "author_name", "assigned_to", "assigned_to_name", "table", "table_name",
            "created_at", "updated_at",
        )


class TaskListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    assigned_to_name = serializers.CharField(source="assigned_to.username", read_only=True, default=None)

    class Meta:
        model = Task
        fields = ("id", "title", "status", "priority", "deadline", "author_name", "assigned_to_name", "created_at",)



class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("status", "priority", "assigned_to", "deadline",)


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "task", "user", "user_name", "text", "created_at",)
