from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import mixins, viewsets, status

from .models import Board, Table, Task, Comment
from .serializers import (
    BoardSerializer, TableSerializer, TaskSerializer,
    TaskListSerializer, TaskUpdateSerializer, CommentSerializer
)


class BoardViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class TableViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["board"]


class TaskViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["table", "status", "assigned_to"]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["author"] = request.user.id

        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)


class TaskUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer


class TaskDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        task_id = kwargs.get("pk")
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({"success": "Задача удалена"}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Задача не найдена"}, status=status.HTTP_404_NOT_FOUND)


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.request.query_params.get("task")
        if not task_id:
            raise NotFound("Укажите task в параметрах запроса.")

        return Comment.objects.filter(task_id=task_id)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = request.user.id

        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()

        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
